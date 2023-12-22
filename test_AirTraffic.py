import unittest
from unittest.mock import patch
from AirTraffic import Airplane

class AirplaneTest(unittest.TestCase):
    def test_landing_function(self):
        """
        Test case for the landing_function method of the Airplane class.

        This test case verifies that the landing_function method correctly prints a message when an airplane lands.
        """
        airplane = Airplane(1)
        with patch('builtins.print') as mock_print:
            airplane.landing_function()
            mock_print.assert_called_with("[AC]: Airplane 1 has landed")

    def test_proceed_to_taxiways(self):
        """
        Test case for the proceed_to_taxiways method of the Airplane class.

        This test case verifies that the proceed_to_taxiways method correctly prints a message when an airplane queues in a taxiway.
        """
        airplane = Airplane(1)
        airplane.id = 1
        airplane.runway_array = [1, 0, 0]
        airplane.taxiway_array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        airplane.runway_sem = threading.Semaphore()
        with patch('builtins.print') as mock_print:
            airplane.proceed_to_taxiways()
            mock_print.assert_called_with("[AC]: Airplane 1 queuing in taxiway of runway 1")

    def test_proceed_to_gate(self):
        """
        Test case for the proceed_to_gate method of the Airplane class.

        This test case verifies that the proceed_to_gate method correctly prints a message when an airplane is assigned a gate.
        """
        airplane = Airplane(1)
        airplane.id = 1
        airplane.taxiway_array = [[0, 0, 0], [0, 0, 0], [1, 0, 0]]
        airplane.gate_array = [0, 0, 0]
        airplane.gate_sem = threading.Semaphore()
        with patch('builtins.print') as mock_print:
            airplane.proceed_to_gate()
            mock_print.assert_called_with("[GC]: Airplane 1 assigned gate 1")

    def test_proceed_to_hangar(self):
        """
        Test case for the proceed_to_hangar method of the Airplane class.

        This test case verifies that the proceed_to_hangar method correctly prints a message when an airplane heads to the hangar.
        """
        airplane = Airplane(1)
        airplane.id = 1
        airplane.gate_array = [1, 0, 0]
        airplane.gate_sem = threading.Semaphore()
        with patch('builtins.print') as mock_print:
            airplane.proceed_to_hangar()
            mock_print.assert_called_with("[AC]: Airplane 1 heading to hangar")

if __name__ == '__main__':
    unittest.main()