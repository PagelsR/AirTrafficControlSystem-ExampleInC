import threading
import time
import queue

class Airplane:
    def __init__(self, id: int):
        """Initialize an Airplane with an id."""
        self.id = id

class Runway:
    NUMBER_OF_RUNWAYS = 2
    NUMBER_OF_GATES = 1
    NUMBER_OF_AIRPLANES = 9

    def __init__(self):
        """Initialize a Runway with queues for runways, taxiways, and gates."""
        self.runway_queue = queue.Queue(self.NUMBER_OF_RUNWAYS)
        self.taxiway_queue = [queue.Queue(3) for _ in range(self.NUMBER_OF_RUNWAYS)]
        self.gate_queue = queue.Queue(self.NUMBER_OF_GATES)

    def landing_function(self, airplane: Airplane):
        """Handle the landing of an airplane."""
        print(f"[AC]: Flight {airplane.id} requesting landing")
        self.runway_queue.put(airplane.id)
        print(f"[GC]: Airplane {airplane.id} assigned runway {self.runway_queue.queue.index(airplane.id) + 1}")
        print(f"[AC]: Airplane {airplane.id} has landed")

    def proceed_to_taxiways(self, airplane: Airplane):
        """Move an airplane from the runway to a taxiway."""
        for taxiway in self.taxiway_queue:
            if not taxiway.full():
                taxiway.put(airplane.id)
                self.runway_queue.get()
                print(f"[AC]: Airplane {airplane.id} queuing in taxiway of runway {self.taxiway_queue.index(taxiway) + 1}")
                break