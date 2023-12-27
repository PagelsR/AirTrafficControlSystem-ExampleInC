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
        self.id = id
        self.thread = threading.Thread(target=self.airplane_control)

    def landing_function(self):
        print(f"[AC]: Flight {self.id} requesting landing")
        runway_sem.acquire()
        stop = False
        for i in range(NUMBER_OF_RUNWAYS):
            if runway_array[i] == 0 and (taxiway_array[i][0] == 0 or taxiway_array[i][1] == 0 or taxiway_array[i][2] == 0) and queue_sem[i].acquire(blocking=False):
                runway_array[i] = self.id
                stop = True
                break
        print(f"[GC]: Airplane {self.id} assigned runway {i + 1}")
        print(f"[AC]: Airplane {self.id} has landed")

    def proceed_to_taxiways(self):
        runway = next(i for i in range(NUMBER_OF_RUNWAYS) if runway_array[i] == self.id)
        for j in range(3):
            if taxiway_array[runway][j] == 0:
                taxiway_array[runway][j] = self.id
                runway_array[runway] = 0
                runway_sem.release()
                break
        print(f"[AC]: Airplane {self.id} queuing in taxiway of runway {runway + 1}")

    def proceed_to_gate(self):
        print(f"[AC]: Airplane {self.id} requesting gate")
        gate_sem.acquire()
        for i in range(NUMBER_OF_RUNWAYS):
            for j in range(3):
                if taxiway_array[i][j] == self.id:
                    queue_sem[i].release()
                    taxiway_array[i][j] = 0
                    break
        for i in range(NUMBER_OF_GATES):
            if gate_array[i] == 0:
                gate_array[i] = self.id
                break
        print(f"[GC]: Airplane {self.id} assigned gate {i + 1}")

    def proceed_to_hangar(self):
        time.sleep(5)
        print(f"[AC]: Airplane {self.id} heading to hangar")
        for i in range(NUMBER_OF_GATES):
            if gate_array[i] == self.id:
                gate_array[i] = 0
                gate_sem.release()
                break

    def airplane_control(self):
        self.landing_function()
        self.proceed_to_taxiways()
        self.proceed_to_gate()
        self.proceed_to_hangar()

def main():
    airplanes = [Airplane(i+1) for i in range(NUMBER_OF_AIRPLANES)]
    for airplane in airplanes:
        airplane.thread.start()
    for airplane in airplanes:
        airplane.thread.join()

if __name__ == "__main__":
    main()