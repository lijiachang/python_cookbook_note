import sys
import types
import operator


def named_tuple(clss_name, field_names):
    # 访问字段通过property
    cls_dict = {name: property(operator.itemgetter(n)) for n, name in enumerate(field_names)}

    # 生成一个__new__ 添加到类字典中
    def __new__(cls, *args):
        if len(args) != len(field_names):
            raise TypeError('Expected {} arguments'.format(len(field_names)))
        return tuple.__new__(cls, args)

    cls_dict['__new__'] = __new__

    cls = types.new_class(clss_name, (tuple,), {}, lambda ns: ns.update(cls_dict))
    cls.__module__ = sys._getframe(1).f_globals['__name__']  # 获取调用者所在的模块名称

    return cls


Point = named_tuple('Point', ['x', 'y'])
print(Point)

p = Point(4, 5)
print(len(p))
print(p.x)

p.x = 444  # AttributeError: can't set attribute

