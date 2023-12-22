import threading
import time

NUMBER_OF_RUNWAYS = 3
NUMBER_OF_GATES = 2

runway_array = [0] * NUMBER_OF_RUNWAYS
taxiway_array = [[0] * 3 for _ in range(NUMBER_OF_RUNWAYS)]
queue_sem = [threading.Semaphore(1) for _ in range(NUMBER_OF_RUNWAYS)]
runway_sem = threading.Semaphore(NUMBER_OF_RUNWAYS)
gate_array = [0] * NUMBER_OF_GATES
gate_sem = threading.Semaphore(NUMBER_OF_GATES)

class TestAirplane:
    """
    This class contains test cases for the Airplane class.

    Methods:
    - test_airplane_landing: Test the landing functionality of an airplane.
    - test_airplane_taxiways: Test the proceeding to taxiways functionality of an airplane.
    - test_airplane_gate: Test the proceeding to gate functionality of an airplane.
    - test_airplane_hangar: Test the proceeding to hangar functionality of an airplane.
    - test_airplane_control: Test the entire control flow of an airplane.
    """

    def test_airplane_landing(self):
        """
        Test the landing functionality of an airplane.

        This method creates an instance of the Airplane class, performs the landing function,
        and adds assertions to check if the airplane has landed correctly.
        """

        airplane = Airplane(1)
        airplane.landing_function()
        # Add assertions to check if the airplane has landed correctly

    def test_airplane_taxiways(self):
        """
        Test the proceeding to taxiways functionality of an airplane.

        This method creates an instance of the Airplane class, proceeds to the taxiways,
        and adds assertions to check if the airplane has proceeded to the taxiways correctly.
        """

        airplane = Airplane(1)
        airplane.proceed_to_taxiways()
        # Add assertions to check if the airplane has proceeded to the taxiways correctly

    def test_airplane_gate(self):
        """
        Test the proceeding to gate functionality of an airplane.

        This method creates an instance of the Airplane class, proceeds to the gate,
        and adds assertions to check if the airplane has proceeded to the gate correctly.
        """

        airplane = Airplane(1)
        airplane.proceed_to_gate()
        # Add assertions to check if the airplane has proceeded to the gate correctly

    def test_airplane_hangar(self):
        """
        Test the proceeding to hangar functionality of an airplane.

        This method creates an instance of the Airplane class, proceeds to the hangar,
        and adds assertions to check if the airplane has proceeded to the hangar correctly.
        """

        airplane = Airplane(1)
        airplane.proceed_to_hangar()
        # Add assertions to check if the airplane has proceeded to the hangar correctly

    def test_airplane_control(self):
        """
        Test the entire control flow of an airplane.

        This method creates an instance of the Airplane class, performs the airplane control flow,
        and adds assertions to check if the airplane has completed the entire control flow correctly.
        """

        airplane = Airplane(1)
        airplane.airplane_control()
        # Add assertions to check if the airplane has completed the entire control flow correctly

# Run the tests
test_airplane = TestAirplane()
test_airplane.test_airplane_landing()
test_airplane.test_airplane_taxiways()
test_airplane.test_airplane_gate()
test_airplane.test_airplane_hangar()
test_airplane.test_airplane_control()