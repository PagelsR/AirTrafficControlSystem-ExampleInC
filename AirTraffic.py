import threading
import time
import queue

NUMBER_OF_RUNWAYS = 2
NUMBER_OF_GATES = 1
NUMBER_OF_AIRPLANES = 9

class Airplane:
    def __init__(self, id):
        self.id = id

class Runway:
    def __init__(self):
        self.runway_queue = queue.Queue(NUMBER_OF_RUNWAYS)
        self.taxiway_queue = [queue.Queue(3) for _ in range(NUMBER_OF_RUNWAYS)]
        self.gate_queue = queue.Queue(NUMBER_OF_GATES)

    def landing_function(self, airplane):
        print(f"[AC]: Flight {airplane.id} requesting landing")
        self.runway_queue.put(airplane.id)
        print(f"[GC]: Airplane {airplane.id} assigned runway {self.runway_queue.queue.index(airplane.id) + 1}")
        print(f"[AC]: Airplane {airplane.id} has landed")

    def proceed_to_taxiways(self, airplane):
        for taxiway in self.taxiway_queue:
            if not taxiway.full():
                taxiway.put(airplane.id)
                self.runway_queue.get()
                print(f"[AC]: Airplane {airplane.id} queuing in taxiway of runway {self.taxiway_queue.index(taxiway) + 1}")
                break

    def proceed_to_gate(self, airplane):
        print(f"[AC]: Airplane {airplane.id} requesting gate")
        for taxiway in self.taxiway_queue:
            if airplane.id in taxiway.queue:
                taxiway.queue.remove(airplane.id)
                self.gate_queue.put(airplane.id)
                print(f"[GC]: Airplane {airplane.id} assigned gate {self.gate_queue.queue.index(airplane.id) + 1}")
                break

    def proceed_to_hangar(self, airplane):
        time.sleep(5)
        print(f"[AC]: Airplane {airplane.id} heading to hangar")
        self.gate_queue.get()

def airplane_control(airplane, runway):
    runway.landing_function(airplane)
    runway.proceed_to_taxiways(airplane)
    runway.proceed_to_gate(airplane)
    runway.proceed_to_hangar(airplane)

def main():
    runway = Runway()
    airplanes = [Airplane(i+1) for i in range(NUMBER_OF_AIRPLANES)]
    threads = []

    for airplane in airplanes:
        thread = threading.Thread(target=airplane_control, args=(airplane, runway))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
    