class Node:
    """使用Node类表示树结构，实现一个迭代器能够以深度优先的模式遍历树的节点"""

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
        yield self
        for c in self:
            yield from c.depth_first()


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
