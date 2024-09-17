import time
from queue import Queue
import threading

_sentinel = object()


def producer(q: Queue):
    n = 0
    while n < 3:
        time.sleep(1)
        q.put(n)
        n += 1

    # put the sentinel on the queue to indicate completion
    q.put(_sentinel)


def consumer(q: Queue):
    while True:
        result = q.get()

        # check for termination
        if result is _sentinel:
            print("consumer termination!")
            q.put(_sentinel)  # 重新放回，让其他消费者也能正常退出
            break

        print("consumer get: ", result)


q = Queue()
t1 = threading.Thread(target=producer, args=(q,))
t2 = threading.Thread(target=consumer, args=(q,))
t1.start()
t2.start()
