from inspect import signature
import logging


class MathSignaturesMeta(type):
    def __init__(self, cls_name, bases, cls_dict):
        super().__init__(cls_name, bases, cls_dict)
        sup = super(self, self)
        for name, value in cls_dict.items():
            # 过滤掉私有方法和属性
            if name.startswith('_') or not callable(value):
                continue
            # 获取之前的定义（如果有）然后对比签名
            prev_dfn = getattr(sup, name, None)
            if prev_dfn:
                prev_sign = signature(prev_dfn)
                value_sign = signature(value)
                if prev_sign != value_sign:
                    logging.warning('Signature mismatch in %s.  %s != %s', value.__qualname__, value_sign, prev_sign)


class Root(metaclass=MathSignaturesMeta):
    pass


class A(Root):
    def foo(self, x, y):
        pass

    def spam(self, x, *, z):
        pass


class B(A):
    def foo(self, a, b):
        pass

    def spam(self, x, z):
        pass
