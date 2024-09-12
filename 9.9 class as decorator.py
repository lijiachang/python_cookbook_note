import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)  # 作用在self上

        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)  # 通过__wrapped__属性用于functools.warp装饰的元数据。

    def __get__(self, instance, owner):
        """
        self 指Profiled实例
        instance 指Spam实例
        owner 指Spam类对象
        """

        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)  # 将方法绑定到类实例中（或绑定到类方法）


@Profiled
def add(x, y):
    return x + y


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


print(add(1, 2))
print(add(2, 3))
print(add.ncalls)

a = Spam()
a.bar(1)
a.bar(2)
print(Spam.bar.ncalls)
