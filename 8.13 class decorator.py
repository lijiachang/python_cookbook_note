class Descriptor:
    """基类，使用描述符设置属性"""

    def __init__(self, name=None, **opts):
        self.name = name
        for k, v in opts.items():
            setattr(self, k, v)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __get__(self, instance, cls):
        """注意：书中的代码并没有设置__get__方法，但是获取实例属性会出现<__main__.SizedString object at 0x100db2c40>
        所以这里定义了__get__"""
        if instance is None:
            return self
        return instance.__dict__[self.name]


def Typed(expected_type, cls=None):
    if cls is None:
        return lambda cls: Typed(expected_type, cls)

    super_set = cls.__set__

    def __set__(self, instance, value):
        if not isinstance(value, expected_type):
            raise TypeError('Expected ' + str(expected_type))
        super_set(self, instance, value)

    cls.__set__ = __set__

    return cls


def Unsigned(cls):
    super_set = cls.__set__

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super_set(self, instance, value)

    cls.__set__ = __set__

    return cls


def MaxSized(cls):
    super_init = cls.__init__

    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super_init(self, name, **opts)

    cls.__init__ = __init__

    super_set = cls.__set__

    def __set__(self, instance, value):
        if len(value) > self.size:
            raise ValueError('size must be < ' + str(self.size))
        super_set(self, instance, value)

    cls.__set__ = __set__

    return cls


@Typed(int)
class Integer(Descriptor):
    pass


@Unsigned
class UnsignedInteger(Integer):
    pass


@Typed(float)
class Float(Descriptor):
    pass


@Unsigned
class UnsignedFloat(Float):
    pass


@Typed(str)
class String(Descriptor):
    pass


@MaxSized
class SizedString(String):
    pass


class Stock:
    name = SizedString(size=8)

    def __init__(self, name):
        self.name = name


s = Stock('AC')
print(s.name)
