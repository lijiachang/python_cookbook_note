from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    def decorator(func):
        if not __debug__:  # Python默认__debug__为True，需要python -o为性能模式optimized 此时断言等代码不会执行。
            return func

        # 用dict存储提供的类型
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # 强制类型检查
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@typeassert(int, int)
def add(x, y):
    return x + y


# print(add(1, 2))
#
# print(add('1', '2')) # TypeError: Argument x must be <class 'int'>

# @typeassert(int, z=int)
# def spam(x, y, z=42):
#     print(x, y, z)
#
#
# spam(1, 2, 3)
# spam(1, 'hello', 3)
# spam(1, 'hello', 'world')  # TypeError: Argument z must be <class 'int'>

@typeassert(int, list)
def bar(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items

print(bar(2))
print(bar(2, [1, 2, 3]))
print(bar(2, 3))