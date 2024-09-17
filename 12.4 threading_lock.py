import threading


class SharedCounter:
    """
    可以在多线程中共享
    """
    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta=1):
        with self._value_lock:
            self._value += delta

    def decr(self, delta=1):
        with self._value_lock:
            self._value -= delta
