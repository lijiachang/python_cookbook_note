class lazyproperty:
    """装饰器：让方法只执行一次，再次访问时使用缓存"""

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('computing area')
        return math.pi * self.radius ** 2


c = Circle(4.0)
# print(c.radius)
# print(c.area)
# print(c.area)  # 第二次访问area属性，并没有打印 'computing area'

c = Circle(4.0)
print(vars(c))
print(c.area)
print(vars(c))

del c.area
print(vars(c))
print(c.area)