class LoggedMappingMixin:
    """为了记录debug增加get、set、delete操作"""
    __slots__ = ()

    def __getitem__(self, item):
        print('getting ' + str(item))
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        print('setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('deleting ' + str(key))
        return super().__delitem__(key)


class SetOnceMappingMixin:
    """只运行key被设置一次"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class StringKeyMappingMixin:
    """约束key只能是string"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be string')
        return super().__setitem__(key, value)


# 1. log观察dict的操作
# class LoggedDict(LoggedMappingMixin, dict):
#     pass
#
#
# d = LoggedDict()
# d['x'] = 123
# print(d['x'])
# del d['x']

# 2. 不能重复set的dict
# from collections import defaultdict
#
#
# class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
#     pass
#
#
# d = SetOnceDefaultDict(list)
# d['x'].append(2)
# d['y'].append(3)
# d['x'] = 23

from collections import OrderedDict


class StringOrderedDict(StringKeyMappingMixin, SetOnceMappingMixin, OrderedDict):
    pass


d = StringOrderedDict()
d['x'] = 23
d[42] = 10  # TypeError: keys must be string
d['x'] = 24  # KeyError: 'x already set'
