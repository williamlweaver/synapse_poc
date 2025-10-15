SYNAPSE Proof-of-Concept: The Complete Tutorial

1. Mission Briefing: The Why

In the world of scientific instrumentation, researchers often face a difficult choice. On one side are powerful but expensive, proprietary, "closed-box" systems (like LabVIEW running on Windows). These systems can be inflexible and often rely on deprecated toolkits, leaving innovators stranded when new hardware emerges. On the other side is the vast, open universe of modern tools like Python, JavaScript, and powerful microcontrollers like the Arduino.

This project, the SYNAPSE Proof-of-Concept (POC), is the first step in bridging that gap. Our mission is to build a complete, working instrumentation system from the ground up using a modern, open-source technology stack. We will prove that we can create a system that is responsive, powerful, and free from the constraints of proprietary software.

This tutorial documents the successful creation of a simple but complete data acquisition and control system, paving the way for the full SYNAPSE (SYNchronized Acquisition & Python Scripting Environment) framework.

2. Mission Objectives

By the end of this tutorial, you will have:

Assembled a complete hardware circuit with a sensor (potentiometer) and two actuators (a servo motor and an LED).

Programmed an Arduino Uno to act as a passive, real-time hardware peripheral.

Written a Python script to act as the central "brain" of the system, handling logic and data processing.

Created a modern, web-based user interface with JavaScript that can control the hardware and display live data from any web browser.

Successfully integrated all three layers (Hardware, Firmware, and Software) into a single, cohesive, and fully functional system.

3. System Components

Hardware (The "Vessel")

1x Arduino Uno R3

1x USB A-to-B Cable

1x Solderless Breadboard

1x SG90 Servo Motor

1x 10kΩ Potentiometer

1x LED (any color)

1x 220Ω Resistor (for the LED)

Jumper Wires

An external 5V power supply for the breadboard (recommended for stability)

Software (The "Flight Computers")

Arduino IDE: For uploading firmware to the Arduino. Download here

Python (version 3.7+): The core of our system's intelligence. Download here

Visual Studio Code (VS Code): Our recommended code editor, or "shipyard." Download here

A modern web browser (Chrome, Firefox, Edge)

4. The Step-by-Step Assembly and Launch Sequence

Part 1: Hardware Assembly (The "Green" and "Red" Layers)

First, we will build the physical vessel. This circuit separates the high-power motor from the sensitive Arduino logic and provides a common ground for reliable communication.

Circuit Diagram:

Connections:

Power Setup:

Connect your external 5V power supply to the power rails of your breadboard.
Crucially, connect a ground (GND) pin from the Arduino to the blue ground rail on the breadboard. This establishes a "common ground," which is essential for all components to communicate reliably.

Potentiometer (Input Sensor):
Connect the outer two pins to the 5V and Ground rails on the breadboard.
Connect the center pin to pin A0 on the Arduino.

Servo Motor (Output Actuator):
Connect the Brown wire to the Ground rail.
Connect the Red wire to the 5V rail.
Connect the Orange (signal) wire to pin 9 on the Arduino.

LED (Output Actuator):
Connect the 220Ω resistor from pin 11 on the Arduino to the breadboard.
Connect the longer leg (anode) of the LED to the other end of the resistor.
Connect the shorter leg (cathode) of the LED to the Ground rail.

Part 2: The Firmware (The Peripheral's "Operating System")

Next, we load the intelligence onto our hardware peripheral. This firmware makes the Arduino a passive listener, waiting for commands from the Python brain.

Open the Arduino IDE.
Copy the complete contents of the arduino_firmware_final.ino file and paste it into the Arduino IDE window.
Connect your Arduino Uno to your PC via USB.Ensure the correct Board (Arduino Uno) and Port are selected under the Tools menu.
Click the "Upload" button.

Part 3: The Python Backend (The System's "Brain")

Now, we set up the central nervous system on our PC.

Create the Project Folder:On your computer, create a new folder for the project (e.g., synapse-poc).
Inside that folder, create another folder named templates. This is where Flask will look for HTML files.

Create the Python File:
Inside the main synapse-poc folder, create a new file named synapse_poc_final.py.
Copy the contents of the provided synapse_poc_final.py file into this new file.

Install Python Libraries:
Open a command prompt or terminal directly in your synapse-poc folder. (In VS Code, use Terminal -> New Terminal).
Run the following command to install all the necessary libraries:

pip install pyserial flask flask-socketio simple-websocket eventlet

Part 4: The Web Interface (The "Bridge Viewscreen")

Finally, we create the user interface.

Create the HTML File:

Inside the templates folder you created, make a new file named index_final.html.
Copy the complete contents of the provided index_final.html file into this new file.
Your final file structure should look exactly like this:synapse-poc/
|-- synapse_poc.py
|-- templates/
    |-- index_final.html
    
Part 5: Launch Sequence!

Make sure your Arduino is plugged into your PC.
In your command prompt/terminal (still inside the synapse-poc folder), run the Python script:

python synapse_poc.py

You will see terminal output indicating the server has started.

Open your web browser and navigate to the address: http://127.0.0.1:5000

You should now see the SYNAPSE interface, a "Connected" status, and have full control over the LED and see live updates from the potentiometer and servo.

5. Mission Debriefing

Congratulations! You have successfully built a complete, multi-layered data acquisition and control system using modern, open-source tools. This POC validates the core principles of the SYNAPSE architecture: a passive, real-time hardware layer controlled by an intelligent Python backend, with a flexible, decoupled web-based UI.

This successful "shakedown cruise" proves the design is sound. We now have a tangible, working model, ready to be scaled up and adapted when the next-generation Arduino Q hardware arrives. The foundation is laid for a new era of open, accessible, and powerful scientific instrumentation.
