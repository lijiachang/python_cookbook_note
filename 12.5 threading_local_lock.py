import threading
from contextlib import contextmanager

# thread-local state to stored information on locks already acquired
_local = threading.local()  # 创建一个线程本地存储 _local，用于存储每个线程已经获取的锁的信息。


@contextmanager
def acquire(*locks):
    """用于多线程编程中安全获取多个锁的上下文管理器"""
    locks = sorted(locks, key=lambda x: id(x))

    # make sure lock order of previously acquired locks is not violated
    acquired = getattr(_local, "acquired", [])  # 获取当前线程已经获取的锁列表。
    # 如果已获取的锁中有 id 大于等于即将获取的第一个锁的 id，则抛出异常。这是为了确保锁的获取顺序一致，防止死锁。
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError("Lock Order Violated")

    # acquired all of the locks
    acquired.extend(locks)
    _local.acquired = acquired
    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # release locks in reverse order of acquisition
        for lock in reversed(locks):  # 锁的释放顺序与获取顺序相反。
            lock.release()
        del acquired[-len(locks):]


import threading

x_lock = threading.Lock()
y_lock = threading.Lock()


def thread_1():
    while True:
        # with acquire(x_lock, y_lock):
        with acquire(x_lock):
            with acquire(y_lock):
                print("Thread-1")


def thread_2():
    while True:
        # with acquire(y_lock, x_lock):
        with acquire(y_lock):
            with acquire(x_lock):
                print("Thread-2")


t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()
