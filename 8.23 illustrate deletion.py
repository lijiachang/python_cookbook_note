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

    def add_children(self, child):
        self.children.append(child)
        child.parent = self


a = Date()
del a  # 会立即删除

a = Node()
del a  # 也会立即删除

a = Node()
b = Node()
a.add_children(b)
del a  # 不会立即删除

time.sleep(1000)  # 防止脚本退出，从而强制垃圾回收
