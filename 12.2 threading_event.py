from threading import Thread, Event
import time

def countdown(n, started_event: Event):
    print("countdown starting")
    started_event.set()
    while n>0:
        print("T-minus", n)
        n -= 1
        time.sleep(5)

# create the event object that will be used to signal startup
started_event = Event()

# launch the thread and pass the startup event
print("launching countdown")
t = Thread(target=countdown, args=(3, started_event))
t.start()

# wait for the thread to start
started_event.wait()
print("countdown is running")