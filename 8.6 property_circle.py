import math


class Circle:
    def __init__(self, radius):
        """radius: 半径"""
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        """perimeter: 周长"""
        return 2 * math.pi * self.radius


c = Circle(4.0)
print(c.radius)
print(c.area)
print(c.perimeter)
