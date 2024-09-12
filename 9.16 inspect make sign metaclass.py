from inspect import Signature, Parameter


def make_sign(*names):
    params = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(params)


class StructureMeta(type):
    def __new__(cls, cls_name, bases, cls_dict):
        cls_dict['__signature__'] = make_sign(*cls_dict.get('_fields', []))
        return super().__new__(cls, cls_name, bases, cls_dict)


class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    _fields = ['name', 'shares', 'price']


# 演示
import inspect
print(inspect.signature(Stock))

s1 = Stock('ACME', 100, 12.2)
print(s1.name)
