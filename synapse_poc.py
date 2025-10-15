import serial
import time
import threading
from flask import Flask, render_template
from flask_socketio import SocketIO
import serial.tools.list_ports

# --- Configuration ---
# Leave ARDUINO_PORT as None to auto-detect, or set to a specific port e.g., 'COM3'
ARDUINO_PORT = None
BAUD_RATE = 9600

# --- Global Variables ---
# The 'templates' folder is a Flask convention.
# The app object needs to know this to find the index.html file.
app = Flask(__name__, template_folder='templates')
socketio = SocketIO(app)
ser = None  # Serial object for Arduino communication

# --- Helper Functions ---
def find_arduino_port():
    """Scans for available serial ports and returns the one with an Arduino."""
    ports = serial.tools.list_ports.comports()
    for port in ports:
        # A simple check for common Arduino identifiers
        if "Arduino" in port.description or "CH340" in port.description:
            return port.device
    return None

def connect_to_arduino():
    """Establishes a serial connection to the Arduino."""
    global ser
    port_to_use = ARDUINO_PORT if ARDUINO_PORT else find_arduino_port()
    
    if not port_to_use:
        print("Error: Could not find Arduino. Please check connection and port.")
        return False

    try:
        print(f"Attempting to connect to Arduino on {port_to_use}...")
        ser = serial.Serial(port_to_use, BAUD_RATE, timeout=1)
        time.sleep(2)  # Wait for the serial connection to initialize
        print("Arduino connected successfully.")
        return True
    except serial.SerialException as e:
        print(f"Error connecting to {port_to_use}: {e}")
        return False

# --- Background Thread for Arduino Communication ---
def read_from_arduino():
    """
    Runs in a background thread. This is the core of the request-response loop.
    It periodically requests sensor data from the Arduino and handles the response.
    """
    while True:
        if ser and ser.is_open:
            try:
                # 1. Request a new sensor reading from the Arduino.
                # The 'R' stands for "Read". The '\n' is the newline character
                # that the Arduino firmware is now expecting to signify the end of a command.
                ser.write(b'R\n')

                # 2. Read the response from the Arduino.
                # ser.readline() waits for a complete line (ending in '\n').
                line = ser.readline().decode('utf-8').strip()

                if line.startswith('A'):
                    # Potentiometer data received (e.g., "A512")
                    pot_value_str = line[1:]
                    try:
                        pot_value = int(pot_value_str)
                        # Map the 0-1023 analog value to a 0-180 servo angle
                        servo_angle = int(pot_value * (180.0 / 1023.0))
                        
                        # Send the calculated servo command back to the Arduino
                        servo_command = f"S{servo_angle}\n"
                        ser.write(servo_command.encode('utf-8'))
                        # This print is for debugging in the terminal
                        # print(f"Sent to Arduino: S{servo_angle}")

                        # Emit data to the web interface via SocketIO for UI updates
                        socketio.emit('update_sensor', {
                            'pot_value': pot_value,
                            'servo_angle': servo_angle
                        })
                    except (ValueError, IndexError):
                        # This handles cases where the Arduino might send incomplete data
                        print(f"Warning: Malformed data received: '{line}'")

            except serial.SerialException as e:
                print(f"Serial error: {e}")
                break # Exit the loop if the Arduino is disconnected

        # This controls the rate of our data requests. 0.05 seconds = 20 Hz.
        # We MUST use socketio.sleep() here instead of time.sleep() to be
        # compatible with the eventlet server. time.sleep() will block the
        # entire server, causing it to hang. socketio.sleep() is a cooperative
        # pause that allows the server to handle other tasks.
        socketio.sleep(0.05)


# --- Flask Web Server Routes ---
@app.route('/')
def index():
    """Serve the main HTML file from the 'templates' folder."""
    return render_template('index.html')

# --- SocketIO Event Handlers ---
@socketio.on('connect')
def handle_connect():
    """Handles a new client connection."""
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    """Handles a client disconnection."""
    print('Client disconnected')

@socketio.on('led_control')
def handle_led_control(data):
    """Receives LED brightness data from the web interface."""
    if ser and ser.is_open:
        try:
            brightness = int(data['brightness'])
            # Create the command and add the essential newline character
            command = f"L{brightness}\n"
            ser.write(command.encode('utf-8'))
            print(f"Sent to Arduino: L{brightness}")
        except (ValueError, KeyError) as e:
            print(f"Error processing LED command: {e}")

# --- Main Application ---
if __name__ == '__main__':
    if connect_to_arduino():
        # Start the background thread using the socketio-safe method.
        # This prevents the eventlet server from interfering with the blocking
        # pyserial calls, which is the root cause of the 1 Hz slowdown.
        socketio.start_background_task(target=read_from_arduino)

        # Start the Flask-SocketIO web server
        print("Starting SYNAPSE Proof-of-Concept Server...")
        print("Navigate to http://127.0.0.1:5000 in your web browser.")
        # use_reloader=False is important to prevent the script from running twice
        socketio.run(app, debug=True, use_reloader=False)
    else:
        print("Could not start server. Please fix Arduino connection.")



