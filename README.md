SYNAPSE Proof-of-Concept

A complete, open-source data acquisition and control system demonstrating a modern alternative to proprietary lab software like LabVIEW. This project uses a Python backend, a web-based JavaScript UI, and an Arduino Uno to create a responsive, real-time instrumentation platform.

This project serves as the successful "shakedown cruise" for the full SYNAPSE (SYNchronized Acquisition & Python Scripting Environment) framework under development.

The Mission: Why This Project Exists

Scientific researchers often rely on expensive, closed-source software that lacks flexibility and support for modern hardware. This project demonstrates that a powerful, flexible, and accessible alternative can be built entirely with open-source tools, freeing innovators from vendor lock-in and empowering them to build the exact instruments they need for cutting-edge research.

Technology Stack

Backend: Python 3

Web Framework: Flask

Real-Time Communication: Flask-SocketIO with Eventlet

Hardware Communication: PySerial

Frontend: HTML5, CSS3, JavaScript (with Socket.IO client)

Hardware: Arduino Uno R3

Quick Start Guide

For those who want to get the system running immediately.

1. Hardware & Firmware 
First, assemble the physical hardware and upload the firmware to the Arduino. For a detailed circuit diagram and step-by-step instructions, please see the Full Project Tutorial.

2. Software Setup & LaunchThese commands should be run from your terminal or the integrated terminal in VS Code.

# 1. Clone this repository to your local machine
git clone [https://github.com/YourUsername/synapse-poc.git](https://github.com/YourUsername/synapse-poc.git)

# 2. Navigate into the project directory
cd synapse-poc

# 3. Install all required Python libraries from the requirements file
pip install -r requirements.txt

# 4. Make sure your Arduino is plugged in, then run the Python server
python synapse_poc_final.py

3. Access the InterfaceOnce the server is running, open your web browser and navigate to:

http://127.0.0.1:5000

You should see the interface, a "Connected" status, and have full control of the system.

Project StructureYour final file structure should look like this to ensure the Flask application can find all the necessary files.synapse-poc/
|-- README.md
|-- TUTORIAL_FINAL.md
|-- requirements.txt
|-- arduino_firmware_final.ino
|-- synapse_poc_final.py
|-- templates/
    |-- index_final.html
   
The Full Briefing

This Quick Start guide is designed for rapid deployment. For a complete understanding of the project's mission, the systems-level thinking behind the design, and a detailed, step-by-step walkthrough of the entire debugging and integration process, please read the complete SYNAPSE Proof-of-Concept: The Complete Tutorial.
