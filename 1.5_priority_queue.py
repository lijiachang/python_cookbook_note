import heapq


class PriorityQueue:
    """实现优先级队列"""

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


# 测试代码
q = PriorityQueue()
# 将元素存入队列
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('rok'), 1)

# 取出元素 (会按照优先级取出)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
