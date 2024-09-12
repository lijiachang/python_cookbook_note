class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # 设置位置参数
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # 设置剩余的关键字参数
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        # 检查剩余的未知关键字参数
        if kwargs:
            raise TypeError('Invalid arguments: {}'.format(','.join(kwargs)))


if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']


    s1 = Stock('AC', 50, 91.1)
    s2 = Stock('AC', shares=50, price=91.1)
