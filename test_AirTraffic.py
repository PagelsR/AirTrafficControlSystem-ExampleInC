import threading
import time
import unittest

# FILEPATH: /C:/Users/RandyPagels/source/repos/AirTrafficControlSystem-ExampleInC/AirTraffic.py

# Define the constants used in the code
NUMBER_OF_RUNWAYS = 3
NUMBER_OF_GATES = 2

# Define the shared resources used in the code
runway_array = [0] * NUMBER_OF_RUNWAYS
taxiway_array = [[0] * 3 for _ in range(NUMBER_OF_RUNWAYS)]
queue_sem = [threading.Semaphore(1) for _ in range(NUMBER_OF_RUNWAYS)]
runway_sem = threading.Semaphore(1)
gate_array = [0] * NUMBER_OF_GATES
gate_sem = threading.Semaphore(1)

class AirplaneTests(unittest.TestCase):
    def test_airplane_landing(self):
        airplane = Airplane(1)
        airplane.landing_function()
        # Assert that the airplane has acquired a runway
        self.assertIn(airplane.id, runway_array)

    def test_airplane_proceed_to_taxiways(self):
        airplane = Airplane(1)
        # Set up the runway and taxiway for the airplane
        runway_array[0] = airplane.id
        taxiway_array[0][0] = airplane.id
        airplane.proceed_to_taxiways()
        # Assert that the airplane has released the runway and acquired a taxiway
        self.assertEqual(runway_array[0], 0)
        self.assertIn(airplane.id, taxiway_array[0])

    def test_airplane_proceed_to_gate(self):
        airplane = Airplane(1)
        # Set up the taxiway and queue for the airplane
        taxiway_array[0][0] = airplane.id
        queue_sem[0].release()
        airplane.proceed_to_gate()
        # Assert that the airplane has released the taxiway and acquired a gate
        self.assertEqual(taxiway_array[0][0], 0)
        self.assertIn(airplane.id, gate_array)

    def test_airplane_proceed_to_hangar(self):
        airplane = Airplane(1)
        # Set up the gate for the airplane
        gate_array[0] = airplane.id
        airplane.proceed_to_hangar()
        # Assert that the airplane has released the gate
        self.assertEqual(gate_array[0], 0)

if __name__ == '__main__':
    unittest.main()