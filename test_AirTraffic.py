import unittest
from AirTraffic import Runway

class TestRunway(unittest.TestCase):
    """
    This class contains unit tests for the Runway class in the AirTraffic module.
    """

    def setUp(self):
        """
        Set up the test fixture. This method is called before each test method.
        """
        self.runway = Runway()

    def test_landing_function(self):
        """
        Test the landing_function method of the Runway class.
        """
        airplane_id = 123
        self.runway.landing_function(airplane_id)
        self.assertEqual(self.runway.runway_queue.queue[0], airplane_id)

    def test_proceed_to_taxiways(self):
        """
        Test the proceed_to_taxiways method of the Runway class.
        """
        airplane_id = 123
        self.runway.landing_function(airplane_id)
        self.runway.proceed_to_taxiways(airplane_id)
        self.assertNotIn(airplane_id, self.runway.runway_queue.queue)
        self.assertIn(airplane_id, self.runway.taxiway_queue[0].queue)

    def test_proceed_to_gate(self):
        """
        Test the proceed_to_gate method of the Runway class.
        """
        airplane_id = 123
        self.runway.landing_function(airplane_id)
        self.runway.proceed_to_taxiways(airplane_id)
        self.runway.proceed_to_gate(airplane_id)
        self.assertNotIn(airplane_id, self.runway.taxiway_queue[0].queue)
        self.assertIn(airplane_id, self.runway.gate_queue.queue)

    def test_proceed_to_hangar(self):
        """
        Test the proceed_to_hangar method of the Runway class.
        """
        airplane_id = 123
        self.runway.landing_function(airplane_id)
        self.runway.proceed_to_taxiways(airplane_id)
        self.runway.proceed_to_gate(airplane_id)
        self.runway.proceed_to_hangar(airplane_id)
        self.assertNotIn(airplane_id, self.runway.gate_queue.queue)

if __name__ == '__main__':
    unittest.main()