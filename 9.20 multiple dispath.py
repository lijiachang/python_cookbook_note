import inspect
import types


class MultiMethod:
    """Represents a single multimethod."""

    def __init__(self, name):
        self._methods = {}
        self.__name__ = name

    def register(self, meth):
        """
        Register a new method as a multimethod
        """
        sig = inspect.signature(meth)

        types_ = []
        for name, param in sig.parameters.items():
            if name == 'self':
                continue
            if param.annotation is inspect.Parameter.empty:
                raise TypeError('Argument {} must be annotated with a type'.format(name))
            if not isinstance(param.annotation, type):
                raise TypeError('Argument {} annotation mest be a type'.format(name))
            if param.default is not inspect.Parameter.empty:
                self._methods[tuple(types_)] = meth
            types_.append(param.annotation)

        self._methods[tuple(types_)] = meth

    def __call__(self, *args):
        types_ = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types_, None)
        if meth:
            return meth(*args)
        else:
            raise TypeError('No matching method for types {}'.format(types_))

    def __get__(self, instance, owner):
        """instance 是实例，owner是实例的类"""
        if instance is not None:
            return types.MethodType(self, instance)  # 给实例动态添加方法。这里将self属性（方法）添加到instance实例中
        else:
            return self


class MultiDict(dict):
    """用元类实现特殊字典去构建多分派函数"""

    def __setitem__(self, key, value):
        if key in self:
            # 如果key已经存在，必须是一个多分派函数或可调用对象
            current_value = self[key]

            if isinstance(current_value, MultiMethod):
                current_value.register(value)
            else:
                mvalue = MultiMethod(key)
                mvalue.register(current_value)
                mvalue.register(value)
                super().__setitem__(key, mvalue)
        else:
            super().__setitem__(key, value)


class MultipleMeta(type):
    """允许多分派的元类"""

    def __new__(cls, cls_name, bases, cls_dict):
        return type.__new__(cls, cls_name, bases, dict(cls_dict))

    @classmethod
    def __prepare__(metacls, name, bases):
        return MultiDict()


# # 示例
# class Spam(metaclass=MultipleMeta):
#     def bar(self, x: int, y: int):
#         print('bar1: ', x, y)
#
#     def bar(self, s: str, n: int = 0):
#         print('bar2: ', s, n)
#
#
# spam = Spam()
# spam.bar(2, 3)
# spam.bar('hello')
#
# spam.bar(2, 'hello')  # TypeError: No matching method for types (<class 'int'>, <class 'str'>)
#

# 示例，多个__init__
# import time
#
#
# class Date(metaclass=MultipleMeta):
#     def __init__(self, year: int, month: int, day: int):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     def __init__(self):
#         t = time.localtime()
#         self.__init__(t.tm_year, t.tm_mon, t.tm_mday)
#
#
# d = Date(2023, 5, 29)
# print(d.day)
#
# e = Date()
# print(e.day)


class A:
    pass


class B(A):
    pass


class C:
    pass


class Spam(metaclass=MultipleMeta):
    def foo(self, x: A):
        print('Foo 1:', x)

    def foo(self, x: C):
        print('Foo 2:', x)


s = Spam()
a = A()
s.foo(a)

c = C()
s.foo(c)

b = B()
s.foo(b)  # TypeError: No matching method for types (<class '__main__.B'>,)
