from inspect import Signature, Parameter


def make_sign(*names):
    params = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(params)


class Structure:
    __signature__ = make_sign()  # 需要子类重写__signature__

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    __signature__ = make_sign('name', 'shares', 'price')


class Point(Structure):
    __signature__ = make_sign('x', 'y')


# 演示
import inspect

print(inspect.signature(Stock))

s1 = Stock('ACME', 100, 120.2)
s2 = Stock('ACME', 100)  # TypeError: missing a required argument: 'price'
