# 只修改lazyproperty
def lazyproperty(func):
    """装饰器：让实例方法只执行一次，再次访问时使用缓存
        并且属性不可变
    """
    name = '_lazy_' + func.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value

    return lazy


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('computing area')
        return math.pi * self.radius ** 2


c = Circle(4.0)
print(c.radius)
print(c.area)
print(c.area)

c.area = 123