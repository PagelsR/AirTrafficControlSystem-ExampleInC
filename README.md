# Air Traffic Control Simulation
An air traffic control simulation in legacy C

## Introduction
Using Copilot to convert C to Python, write unit tests, document unit tests, and generate a commit message.


## This C program is a simulation of an air traffic control system. It uses several libraries, including stdio.h for standard input/output operations, stdlib.h for general purpose functions, pthread.h for multithreading, unistd.h for POSIX operating system API, and semaphore.h for semaphore operations.

### Copilot Demo Walkthrough

This demo shows how Copilot can be used to convert C code to Python, generate unit tests, document unit tests, and generate a commit message.

Demo 1
----------------------------
Open file **AirTraffic.c**

Copilot: type **/Explain**

Speaker
This C program is a simulation of an air traffic control system. It uses several libraries, including stdio.h for standard input/output operations, stdlib.h for general purpose functions, pthread.h for multithreading, unistd.h for POSIX operating system API, and semaphore.h for semaphore operations. The program uses three arrays to represent the state of the airport: gate_array for the gates, runway_array for the runways, and taxiway_array for the taxiways.

Next, let's ask Copilot to convert this to Python.

Demo 2
----------------------------
Speaker
Let's ask Copilot to convert this to Python.  I can highlight the entire file and ask Copilot to convert it to Python.  Copilot will generate the Python code in the chat window.  I can review this, copy it, create a new file, then simply paste in the code.

Copilot: type **Please convert this to Python**

Speaker
This Python code does the same thing as the C code. It creates a number of airplane objects and assigns them to runways, taxiways, and gates using queues. The airplane_control function controls the flow of each airplane from landing to proceeding to the hangar.

Speaker
Copy to clipboard. Cntl-N, to create a new file. Cntrl-V, to paste in code. Cntl-S, to save to **AirTraffic.py**

You can create a new file in Visual Studio Code by clicking on the "New File" icon in the Explorer view or by using the shortcut Ctrl+N. Then, you can paste the above code into the new file. Next, save the file by using the shortcut Ctrl+S.

Demo 3
----------------------------
Speaker
This looks great, thank you Copilot!  As a developer, I will Trust but verify, and run the code to make sure it works as expected.

Next, I want to create unit tests.  I can hightlight one object and easily create a single unit test.

Using Copilot, you can type "write a unit test please" or use the shortcut key /tests.

Highlight **def proceed_to_taxiways(self, airplane)**

Copilot Chat Window
Type **Please write a unit test for this**

Speaker
This will generate a unit test in the Copilot chat window. I can review this, copy it, create a new file, then simply paste in the code.

Another option is to generate all the unit tests for this file. First I'll highlight all the code and then use Copilots inline chat feature to write all my unit tests, let's go ahead and do that now.

Highlight all the lines, then use Copilots shortcut Ctrl+I.
 
Copilot will prompt me right inline and now I can use the shortcut key /tests or simply type "write unit tests everything"

Copilot
Type **/tests**, press <tab>, press <enter>

Speaker
The **TestAirplane** class tests that the id of an Airplane object is correctly set when it is created. The TestAirplaneControl class tests the airplane_control function. It checks that, after calling airplane_control, the airplane has proceeded to the hangar and the runway, taxiway, and gate are all empty.
The **TestGate** class tests the Gate class. It checks that the gate is empty when it is created and that the airplane is assigned to the gate when the assign_airplane function is called.
The **TestRunway** class tests the Runway class. It checks that the runway is empty when it is created and that the airplane is assigned to the runway when the assign_airplane function is called.
The **TestTaxiway** class tests the Taxiway class. It checks that the taxiway is empty when it is created and that the airplane is assigned to the taxiway when the assign_airplane function is called.

Simply click "Create" to save to **test_AirTraffic.py**

Demo 3
----------------------------
Speaker
Next, let's go ahead and document all our unit tests.  This is easily done using Copilot.

There are two options to do this, one is to use the shortcut command /docs to add header comments to classes and objects or ask Copilot to document everything.

Copilot
**create comments for all my classes**, press <enter>

Speaker
Scroll down to show comments above each class.

Demo 4
----------------------------
Speaker
Next, let's use Copilot to generate a good commit message before checking in my code.
Click button **Generate commit message using Copilot**
Click button **Commit and Push**

Demo 5
----------------------------
Speaker
Let's look for ways to improve our code.  Even though my code is well-structured and follows good practices, there's always room for improvement. Copilot can help us with this as well.  Let's ask Copilot to review our code and provide suggestions around performance, security, and style.

Copilot
Type **Please review my code and provide suggestions**

Speaker
Copilot will review the code and provide suggestions in the chat window.  I can review this, copy it, create a new file, then simply paste in the code.

Next, let's use Copilot to generate a good commit message before checking in my code.
Click button **Refactor Runway class to use class variables and type hinting**
Click button **Commit and Push**










### References
### This example is based on the work of Asad Zia located https://github.com/asadzia/Air-Traffic-Control

