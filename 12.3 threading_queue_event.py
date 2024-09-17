import time
from queue import Queue
import threading

def producer(q: Queue):
    n = 0
    while True:
        time.sleep(1)

        # make an (data, event) pair and hand ti to the consumer
        event = threading.Event()
        q.put((n, event))

        # wait for the consumer to process the item
        event.wait()

        n += 1


def consumer(q: Queue):
    while True:
        data, event = q.get()
        print("consumer get: ", data)
        ...
        # indicate completing
        event.set()

