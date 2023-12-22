# Air Traffic Control Simulation
An example air traffic control simulation written using legacy C. This code is setting up the basic structure for an air traffic control system.
- Includes and Constants: Imports libraries and defines constants for runways, gates, airplanes, and mutex conditions.
- Arrays: Declares arrays to represent the state of runways, gates, and taxiways.
- Airplanes Structure: Defines a structure for an airplane with an ID and a thread ID.
- Semaphores: Declares semaphores for runways, gates, and gate queues to manage concurrency.
- Runway Initialization Function: Defines a function to initialize runways, setting all to empty at the start.

## Introduction

This is a walkthrough using Copilot for efficient C to Python code conversion, unit test creation, documentation, commit message generation, and performt efficiency and performance optimizations.

### Copilot Demo Walkthrough

This demo shows how Copilot can be used to convert C code to Python, generate unit tests, document unit tests, and generate a commit message.

Demo 1 - Explain application
----------------------------
Speaker

    Hi, I'm Aria, a DevOps Architect in the Microsoft Service Line USA at Xebia.  I'm going to walkthrough converting legacy see code to Python.  But first, I'm not familiar with this code, so I'll ask Copilot to explain it to me. Copilot will generate detailed comments in the chat window.

Open file **AirTraffic.c**

Copilot Chat Window

- type **/Explain**

Speaker

    This C program is a simulation of an air traffic control system. The program uses three arrays to represent the state of the airport: gate_array for the gates, runway_array for the runways, and taxiway_array for the taxiways.


Demo 2 - Convert C to Python
----------------------------
Speaker

    Let's ask Copilot to convert this to Python.  After highlighting all the code, I will ask Copilot to convert it to Python.  Copilot will generate the Python code in the chat window.  I can review this, copy it, create a new file, then simply paste in the code.

Copilot Chat Window

- type **Please convert this to Python**

Speaker

    This Python code does the same thing as the C code. It creates a number of airplane objects and assigns them to runways, taxiways, and gates using queues. The airplane_control function controls the flow of each airplane from landing to proceeding to the hangar. You can create a new file in Visual Studio Code by using the shortcut Ctrl+N, paste the code into new file, and save by using the shortcut Ctrl+S.

- Copy to clipboard, Cntl-C. Cntl-N, to create a new file. Cntrl-V, to paste in code. Cntl-S, to save to **AirTraffic.py**

Demo 3 - Generate Unit Tests
----------------------------
Speaker

    This looks great, thank you Copilot! As a developer, I will trust but verify, and should run, then debug the code to make sure it works as expected.

    Next, I want to create unit tests. I can hightlight one object and easily create a single unit test.

    Using Copilot, you can type, Please write a unit test for this, or use the shortcut key /tests.

- Open file **AirTraffic.py**
- Highlight **def proceed_to_taxiways(self, airplane)**

Copilot Chat Window

- Type **Please write a unit test for this**

Speaker

    This will generate a unit test in the Copilot chat window. I can review this, copy it, create a new file, then simply paste in the code.

    Another option is to generate all the unit tests for this file. First I'll highlight all the code and then use Copilots inline chat feature to write all my unit tests, let's go ahead and do that now.

    Copilot will prompt me right inline and now I can use the shortcut key /tests or simply type write unit tests everything,

- Highlight all the lines, then use Copilots shortcut Ctrl+I.

Copilot Inline Chat Window

- Type **/tests**, press **Tab**, press **Enter**

Speaker

    The test suite evaluates key aspects of an airplane management system: initializing airplane IDs, checking the functionality of the airplane control function, and ensuring proper assignment and initial conditions of gates, runways, and taxiways. Each test focuses on specific functionalities to guarantee the system's overall effectiveness.

- Simply click **Create** to save to **test_AirTraffic.py**

Demo 4 - Documenting Unit Tests
----------------------------
Speaker

    Next, let's go ahead and document all our unit tests.  This is easily done using Copilot.

    There are two options to do this, one is to use the shortcut command /docs to add header comments to classes and objects or ask Copilot to document everything. Click anywhere in the file and then use Copilots shortcut Ctrl+I.

- Open file **test_AirTraffic.py**
- Put cursor at top of file, then use Copilots shortcut Ctrl+I.

Copilot Inline Chat Window
- Type **document everything**, press **Tab**, press **Enter**

Speaker

- Scroll down to show comments above each class.

Demo 5 - Commit and Push
----------------------------
Speaker
    
    Next, let's use Copilot to generate a good commit message before checking in my code. There are two options to do this, one is to use the shortcut command /commit to generate a commit message or ask Copilot to generate a good commit message.

- Click button **Generate commit message using Copilot**
- Click button **Commit and Push**

Demo 6 - Performance and Security enhancements
----------------------------
Speaker

    Let's look for ways to improve our code.  Even though my code is well-structured and follows good practices, there's always room for improvement. Copilot can help us with this as well.
    
    Let's ask Copilot to review our code and provide suggestions around performance, security, and style.

- Open file **AirTraffic.py**

Copilot Chat Window
- Type **Please review my code and provide suggestions**

Speaker

    Copilot will review the code and provide suggestions in the chat window.  If there are changes to code, I can review the output, copy it to clipboard, create a new file or simply paste in the code in place of original code.

    If you replace the code, don't forget to generate a good commit message before checking in code.

    Thank you for your time today, I hope you enjoyed this demo.  Please reach out to me if you have any questions.

- Click button **Generate commit message using Copilot**
- Click button **Commit and Push**


### References
#### This example is based on the work of Asad Zia located https://github.com/asadzia/Air-Traffic-Control

