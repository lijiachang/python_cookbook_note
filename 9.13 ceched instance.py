import weakref


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cache = weakref.WeakValueDictionary()  # {创建实例的参数: 实例对象}

    def __call__(self, *args):
        # todo 没有**kwargs 这样创建实例的时候 无法使用关键字参数？
        if args in self._cache:
            return self._cache[args]
        else:
            obj = super().__call__(*args)
            self._cache[args] = obj
            return obj


class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name


a = Spam('li')
b = Spam('wang')
c = Spam('li')

print(a is b)
print(a is c)
