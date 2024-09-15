import threading
import time

class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        """
        run the timer and notify waiting threads after each interval
        """
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1  # ^ 是异或（XOR）运算符, 两个位相同结果0，不同为1
                self._cv.notify_all()

    def wait_for_tick(self):
        """
        wait for the next tick of the timer
        """
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()


ptimer = PeriodicTimer(5)
ptimer.start()

# two threads that synchronize on the timer
def countdown(n_ticks):
    while n_ticks > 0:
        ptimer.wait_for_tick()
        print("T-minus", n_ticks)
        n_ticks -= 1

def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print("Counting", n)
        n += 1

threading.Thread(target=countdown, args=(10,)).start()
threading.Thread(target=countup, args=(5,)).start()