import types


class multimethod:
    def __init__(self, func):
        self._methods = {}
        self.__name__ = func.__name__
        self._default = func

    def match(self, *types_):
        def register(func):
            n_defaults = len(func.__defaults__) if func.__defaults__ else 0
            for n in range(n_defaults + 1):
                self._methods[types_[:len(types_) - n]] = func
            return self

        return register

    def __call__(self, *args):
        types_ = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types_, None)
        if meth:
            return meth(*args)
        else:
            return self._default(*args)

    def __get__(self, instance, owner):
        if instance is not None:
            return types.MethodType(self, instance)
        return self


class Spam:
    @multimethod
    def bar(self, *args):
        # 如果没有匹配到类型的默认调用
        raise TypeError('No mathing method for bar')

    @bar.match(int, int)
    def bar(self, x, y):
        print('bar1 :', x, y)

    @bar.match(str, int)
    def bar(self, s, n=0):
        print('bar2 :', s, n)


s = Spam()

s.bar(1, 2)
s.bar('hello')
