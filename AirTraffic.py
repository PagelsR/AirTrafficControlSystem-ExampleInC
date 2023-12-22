import threading
import time
import queue

NUMBER_OF_RUNWAYS = 2
NUMBER_OF_GATES = 1
NUMBER_OF_AIRPLANES = 9

gate_array = [0]*NUMBER_OF_GATES
runway_array = [0]*NUMBER_OF_RUNWAYS
taxiway_array = [[0]*3 for _ in range(NUMBER_OF_RUNWAYS)]

runway_sem = threading.Semaphore(NUMBER_OF_RUNWAYS)
gate_sem = threading.Semaphore(NUMBER_OF_GATES)
queue_sem = [threading.Semaphore(3) for _ in range(NUMBER_OF_RUNWAYS)]

class Airplane:
    def __init__(self, id):
        """
        Initialize an instance of Airplane.

        Args:
            id (int): The unique identifier for the airplane.
        """
        self.id = id
        self.thread = threading.Thread(target=self.airplane_control)

    def landing_function(self):
        """
        Perform the landing function for the airplane.
        """
        runway_sem.acquire()
        stop = False
        for i in range(NUMBER_OF_RUNWAYS):
            if runway_array[i] == 0 and (taxiway_array[i][0] == 0 or taxiway_array[i][1] == 0 or taxiway_array[i][2] == 0) and queue_sem[i].acquire(blocking=False):
                runway_array[i] = self.id
                stop = True
                break

    def proceed_to_taxiways(self):
        """
        Proceed to the available taxiway for the airplane.
        """
        runway = runway_array.index(self.id)
        for j in range(NUMBER_OF_RUNWAYS):
            for k in range(3):
                if taxiway_array[j][k] == 0 and runway_array[j] == self.id:
                    queue_sem[j].acquire()
                    taxiway_array[j][k] = self.id
                    runway_array[j] = 0
                    runway_sem.release()
                    return

    def proceed_to_gate(self):
        """
        Proceed to an available gate for the airplane.
        """
        gate_sem.acquire()
        for j in range(NUMBER_OF_RUNWAYS):
            for i in range(3):
                if taxiway_array[j][i] == self.id:
                    queue_sem[j].release()
                    taxiway_array[j][i] = 0
                    break
        for i in range(NUMBER_OF_GATES):
            if gate_array[i] == 0:
                gate_array[i] = self.id
                break

    def proceed_to_hangar(self):
        """
        Proceed to the hangar for the airplane.
        """
        time.sleep(5)
        for i in range(NUMBER_OF_GATES):
            if gate_array[i] == self.id:
                gate_array[i] = 0
                gate_sem.release()
                break

    def airplane_control(self):
        """
        Control the sequence of actions for the airplane.
        """
        self.landing_function()
        self.proceed_to_taxiways()
        self.proceed_to_gate()
        self.proceed_to_hangar()

if __name__ == "__main__":
    airplanes = [Airplane(i+1) for i in range(NUMBER_OF_AIRPLANES)]
    for airplane in airplanes:
        airplane.thread.start()
    for airplane in airplanes:
        airplane.thread.join()