from collections import OrderedDict


class Typed:
    """各种类型的set描述符"""
    _expect_type = type(None)

    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        """限制类型"""
        if not isinstance(value, self._expect_type):
            raise TypeError('Expect ' + str(self._expect_type))
        instance.__dict__[self._name] = value


class Integer(Typed):
    _expect_type = int


class Float(Typed):
    _expect_type = float


class String(Typed):
    _expect_type = str


class OrderedMeta(type):
    def __new__(cls, cls_name, bases, cls_dict):
        d = dict(cls_dict)
        order = []
        for name, value in cls_dict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order

        return type.__new__(cls, cls_name, bases, d)

    @classmethod
    def __prepare__(metacls, name, bases):
        """
        prepare（创建命名空间）-> 依次执行类定义语句 -> new（创建类）-> init（初始化类）
        元类定义了prepare以后，会最先执行prepare方法，返回一个空的定制的字典，然后再执行类的语句，类中定义的各种属性被收集入定制的字典，最后传给new和init方法。

        3.6版本以前，prepare方法主要用来返回一个orderdict对象，以保存类中属性的添加顺序。而3.6版本以后，默认已经是保持顺序的了。
        """
        return OrderedDict()


class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return ','.join(str(getattr(self, name)) for name in self._order)


# 使用示例
class Stock(Structure):
    """股票"""
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('GOOG', 100, 190.1)
print(s.name)
print(s.as_csv())

s = Stock('GOOG', '100', 190.1)  # TypeError: Expect <class 'int'>
