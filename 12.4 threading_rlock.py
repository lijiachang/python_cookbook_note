import threading


class SharedCounter:
    """
    可以在多线程中共享
    """
    _lock = threading.RLock() #可重入锁允许同一个线程多次获取同一个锁，而不会导致死锁。它会维护一个获取计数器和持有线程的引用。
    def __init__(self, initial_value=0):
        self._value = initial_value

    def incr(self, delta=1):
        with SharedCounter._lock:
            self._value += delta

    def decr(self, delta=1):
        with SharedCounter._lock:
            self.incr(-delta)
