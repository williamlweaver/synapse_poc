/*
  SYNAPSE Proof-of-Concept Firmware (v3 - Final)
  For Arduino Uno R3

  Version 3 addresses two key issues:
  1. PWM Pin Conflict: The LED has been moved from pin 10 to pin 11. The Servo
     library on the Uno disables PWM on pin 10. Pin 11 uses a different hardware
     timer and is not affected.
  2. Protocol: This firmware uses the robust "request-response" model required
     by the final Python script. It only sends data when requested.

  Command Protocol:
  - From Python to Arduino:
    - 'L<val>\n' -> Set LED brightness (PWM). <val> is 0-255.
    - 'S<val>\n' -> Set Servo angle. <val> is 0-180.
    - 'R\n'      -> Request a sensor reading.
  - From Arduino to Python:
    - 'A<val>\n' -> Potentiometer analog reading. <val> is 0-1023. (Sent ONLY on request)
*/

#include <Servo.h>

// --- Pin Definitions ---
const int POT_PIN = A0;   // Potentiometer for servo control
const int SERVO_PIN = 9;  // Servo signal pin
const int LED_PIN = 11;   // <<-- CRITICAL CHANGE: LED moved to Pin 11

// --- Global Objects ---
Servo myServo;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Initialize hardware
  myServo.attach(SERVO_PIN);
  pinMode(LED_PIN, OUTPUT);

  // Set initial states
  myServo.write(90);       // Center the servo
  analogWrite(LED_PIN, 0); // Turn LED off
}

void loop() {
  // The main loop is now very simple. It just listens for commands.
  // The Arduino is now a passive peripheral controlled by the Python "brain".
  handleSerialCommands();
  
  // A tiny delay can help with stability.
  delay(1); 
}

void handleSerialCommands() {
  // Use a robust method to read an entire command terminated by a newline.
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    processCommand(command);
  }
}

void processCommand(String command) {
  // Remove whitespace
  command.trim();
  if (command.length() == 0) return; // Ignore empty commands

  // Check the command prefix to determine the action
  char commandType = command.charAt(0);
  String commandValue = command.substring(1);

  switch (commandType) {
    case 'L': { // LED Command: L<brightness>
      int brightness = commandValue.toInt();
      brightness = constrain(brightness, 0, 255);
      analogWrite(LED_PIN, brightness);
      break;
    }
    case 'S': { // Servo Command: S<angle>
      int angle = commandValue.toInt();
      angle = constrain(angle, 0, 180);
      myServo.write(angle);
      break;
    }
    case 'R': { // Read Sensor Command
      int potValue = analogRead(POT_PIN);
      Serial.print("A");
      Serial.println(potValue);
      break;
    }
  }
}




