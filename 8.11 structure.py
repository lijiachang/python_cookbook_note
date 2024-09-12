class Structure:
    _fields = []  # class variable that specifies expected fields

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # 设置属性
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


if __name__ == '__main__':
    import math


    class Stock(Structure):
        _fields = ['name', 'shares', 'price']


    class Point(Structure):
        _fields = ['x', 'y']


    class Circle(Structure):
        _fields = ['radius']  # radius: 半径

        def area(self):
            return math.pi * self.radius ** 2


    print(Stock('NAME', 50, 91.22))
    print(Point(2, 3))

    print(Stock("NAME", 50))
