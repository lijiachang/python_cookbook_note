import time


class Date:
    """这个类说明del的操作"""

    def __del__(self):
        print('Date.__del__')


class Node:
    def __init__(self):
        self.date = Date()
        self.parent = None
        self.children = []

    # 永远不要这样做，坏的示例
    def __del__(self):
        """说明一个莫名其妙的行为"""
        del self.date
        del self.parent
        del self.children

    def add_children(self, child):
        self.children.append(child)
        child.parent = self


a = Node()
b = Node()
a.add_children(b)
del a  # 不会立即删除

# 即使强制执行垃圾回收也不会
import gc
gc.collect()

# 只有在脚本执行完毕，解释器才会垃圾回收
time.sleep(1000)  # 防止脚本退出，从而强制垃圾回收
