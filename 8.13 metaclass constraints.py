class Descriptor:
    """基类，使用描述符设置属性"""

    def __init__(self, name=None, **opts):
        self.name = name
        for k, v in opts.items():
            setattr(self, k, v)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Type(Descriptor):
    """enforcing types:强制 类型"""
    expected_type = type(None)

    # 限制必须为指定类型
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        super().__set__(instance, value)


class Unsigned(Descriptor):
    """enforcing values:强制 值"""

    # 限制为【无符号整数】，不带有正负号
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super().__set__(instance, value)


class MaxSized(Descriptor):
    """限制实例属性的值，必须小于size大小"""

    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super().__set__(instance, value)


# 下面是不同类似的数据
class Integer(Type):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    """无符号整数"""
    pass


class Float(Type):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    """无符号浮点数"""
    pass


class String(Type):
    expected_type = str


class SizedString(String, MaxSized):
    """限制长度的字符串"""
    pass


class checked_meta(type):
    def __new__(mcs, clsname, bases, methods):
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(mcs, clsname, bases, methods)


class Stock(metaclass=checked_meta):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('AC', 50, 12.34)
s.shares = 1.22
