class MyMeta(type):
    # 可选的
    @classmethod
    def __prepare__(metacls, name, bases, *, debug=False, synchronize=False):
        # 对参数的处理
        ...
        print(debug, synchronize)
        return super().__prepare__(name, bases)

    # 必须的
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # 对参数的处理
        ...
        print(debug, synchronize)
        return super().__new__(cls, name, bases, ns)

    # 必须的
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        # 对参数的处理
        ...
        print(debug, synchronize)
        super().__init__(name, bases, ns)


class Spam(metaclass=MyMeta, debug=True, synchronize=True):
    ...


