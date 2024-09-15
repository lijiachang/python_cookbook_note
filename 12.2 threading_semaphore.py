import threading
import time


def worker(n, sema: threading.Semaphore):
    # wait to be signaled
    sema.acquire() # 如果没有获取到信号量，会被阻塞

    print("working ", n)

semaphore = threading.Semaphore(0)  # 创建了一个初始值为0的信号量。这意味着一开始没有可用的资源。
n_workers = 10
for n in range(n_workers):
    t = threading.Thread(target=worker, args=(n, semaphore))
    t.start()

semaphore.release() # 将信号量的值增加1。这允许一个被阻塞的线程继续执行。
time.sleep(2)
semaphore.release() # 将信号量的值增加1。这允许一个被阻塞的线程继续执行。