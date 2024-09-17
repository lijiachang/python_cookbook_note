import time
from queue import Queue
import threading

def producer(q: Queue):
    n = 0
    while n < 3:
        time.sleep(1)
        q.put(n)
        n += 1

def consumer(q: Queue):
    while True:
        result = q.get()
        print("consumer get: ", result)

        # indicate completion
        q.task_done() # 从队列中获取并处理一个项目后，通知队列该任务已完成

q = Queue()
t1 = threading.Thread(target=producer, args=(q, ))
t2 = threading.Thread(target=consumer, args=(q, ))
t1.start()
t2.start()

# wait for all produced items to consumed
q.join() # 会阻塞主线程，直到队列中的所有项目都被处理完毕（即每个放入队列的项目都调用了 task_done()）