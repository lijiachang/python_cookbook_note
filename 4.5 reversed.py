class Countdown:
    """倒数"""

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        """forward iterator 无穷迭代"""
        n = self.start
        while True:
            yield n
            n -= 1

    def __reversed__(self):
        """reverse iterator """
        n = 1
        while n <= self.start:
            yield n
            n += 1


demo = Countdown(5)
print([x for x in reversed(demo)])
