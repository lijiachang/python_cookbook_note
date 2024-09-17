import threading
import heapq


class PriorityQueue:
    """优先级队列"""

    def __init__(self):
        self._queue = []  # 用列表实现的堆，存储队列项
        self._count = 0  # 解决优先级相同时的排序问题
        self._cv = threading.Condition()  # 条件变量，用于线程同步

    def put(self, item, priority):
        with self._cv:  # 用条件变量锁
            heapq.heappush(self._queue, (-priority, self._count, item))
            # -priority: 负的优先级值，使得高优先级的项排在前面。
            # self._count: 确保相同优先级的项按插入顺序排序。
            self._count += 1
            self._cv.notify_all()  # 通知所有等待(wait())的线程

    def get(self):
        with self._cv:  # 锁保护了对 self._queue 的检查和修改
            while len(self._queue) == 0:
                self._cv.wait()  # 在队列为空时释放锁并等待，直到被 notify_all() 唤醒
            return heapq.heappop(self._queue)[-1]  # 移除并返回具有最高优先级的项。
