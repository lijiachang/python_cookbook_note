import time
from queue import Queue
import threading

def producer(q: Queue):
    n = 0
    while True:
        time.sleep(1)
        q.put(n)
        n += 1

def consumer(q: Queue):
    while True:
        result = q.get()
        print("consumer get: ", result)

q = Queue()
t1 = threading.Thread(target=producer, args=(q, ))
t2 = threading.Thread(target=consumer, args=(q, ))
t1.start()
t2.start()