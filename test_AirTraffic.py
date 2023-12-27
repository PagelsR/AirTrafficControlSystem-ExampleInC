import unittest
from unittest.mock import patch
from io import StringIO

from AirTraffic import Airplane

# Test case for the Airplane class
class AirplaneTestCase(unittest.TestCase):
    def setUp(self):
        self.airplane = Airplane(1)

    # Test the landing_function method
    def test_landing_function(self):
        expected_output = "[AC]: Flight 1 requesting landing\n[GC]: Airplane 1 assigned runway 1\n[AC]: Airplane 1 has landed\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.airplane.landing_function()
            self.assertEqual(fake_output.getvalue(), expected_output)

    # Test the proceed_to_taxiways method
    def test_proceed_to_taxiways(self):
        expected_output = "[AC]: Airplane 1 queuing in taxiway of runway 1\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.airplane.proceed_to_taxiways()
            self.assertEqual(fake_output.getvalue(), expected_output)

    # Test the proceed_to_gate method
    def test_proceed_to_gate(self):
        expected_output = "[AC]: Airplane 1 requesting gate\n[GC]: Airplane 1 assigned gate 1\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.airplane.proceed_to_gate()
            self.assertEqual(fake_output.getvalue(), expected_output)

    # Test the proceed_to_hangar method
    def test_proceed_to_hangar(self):
        expected_output = "[AC]: Airplane 1 heading to hangar\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.airplane.proceed_to_hangar()
            self.assertEqual(fake_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()