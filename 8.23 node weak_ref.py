import weakref


class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({})'.format(self.value)

    @property
    def parent(self):
        print('self._parent: ', self._parent)
        return self._parent if self._parent is None else self._parent()  # 注意：要访问弱引用对象需要加()

    @parent.setter
    def parent(self, value):
        self._parent = weakref.ref(value)

    def add_children(self, children):
        self.children.append(children)
        children.parent = self


root = Node('parent')
c1 = Node('child')

root.add_children(c1)
print(c1.parent)
print(root.children)

del root
print(c1.parent)
