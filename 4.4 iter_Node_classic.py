class Node:
    """使用经典迭代器实现：Node类表示树结构，以深度优先的模式遍历树的节点"""

    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return 'Node({!r})'.format(self.value)

    def add_child(self, node):
        self.children.append(node)

    def __iter__(self):
        return iter(self.children)

    def depth_first(self):
        """深度优先遍历"""
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    """深度优先遍历的迭代器"""
    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        """迭代器的下一个值"""
        # 如果子节点迭代器还没有初始化，则初始化它
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node

        # 如果子节点迭代器已经初始化，则返回下一个子节点
        if self._child_iter is None:
            self._child_iter = next(self._children_iter).depth_first()
        # 如果子节点迭代器已经迭代完毕，则返回下一个节点
        try:
            return next(self._child_iter)
        except StopIteration:
            self._child_iter = None
            return next(self._children_iter)



if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)

    root.add_child(child1)
    root.add_child(child2)

    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
