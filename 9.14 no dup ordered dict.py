from collections import OrderedDict


class NoDupOrderedDict(OrderedDict):
    def __init__(self, cls_name):
        self.cls_name = cls_name
        super().__init__()

    def __setitem__(self, key, value):
        if key in self:
            raise TypeError('{} already in {}'.format(key, self.cls_name))
        super().__setitem__(key, value)


class OrderedMeta(type):
    def __new__(cls, cls_name, bases, cls_dict):
        d = dict(cls_dict)
        d['_order'] = [name for name in cls_dict if name[0] != '_']
        return type.__new__(cls, cls_name, bases, d)

    @classmethod
    def __prepare__(metacls, cls_name, bases):
        return NoDupOrderedDict(cls_name)


class A(metaclass=OrderedMeta):
    """创建重复的属性（方法）就会报错"""
    def spam(self):
        pass

    def spam(self):
        pass

