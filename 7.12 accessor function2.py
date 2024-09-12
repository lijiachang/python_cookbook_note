import sys


class ClosureInstance:  # Closure: 闭包，终止，结束
    def __init__(self, locals=None):
        if locals is None:
            locals: dict = sys._getframe(1).f_locals  # 拿到当前文件对象的所有属性
            # print(sys._getframe(1).f_locals)
            # print(vars())

        # 将可调用对象更新到实例dict
        self.__dict__.update((k, v) for k, v in locals.items() if callable(v))

    def __len__(self):
        return self.__dict__['__len__']()


def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


class Stack2:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


if __name__ == '__main__':
    from timeit import timeit

    s = Stack()
    print(timeit('s.push(1);s.pop()', 'from __main__ import s', number=10000000))

    s2 = Stack2()
    print(timeit('s2.push(1);s2.pop()', 'from __main__ import s2', number=10000000))
