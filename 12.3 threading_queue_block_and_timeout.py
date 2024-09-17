import logging
import queue


q = queue.Queue()

try:
    data = q.get(block=False)
except queue.Empty:
    ...

try:
    data = q.put(block=False)
except queue.Full:
    ...

try:
    data = q.get(timeout=0.5)
except queue.Empty:
    ...


def producer(q: queue.Queue):
    ...
    item = 123
    try:
        q.put(item, block=False)
    except queue.Full:
        logging.warning("queued item %r discarded", item)