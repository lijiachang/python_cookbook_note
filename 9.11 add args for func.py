from functools import wraps


def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):  # 添加了一个额外的debug参数
        if debug:
            print('Calling', func.__name__)
            ...
        return func(*args, **kwargs)

    return wrapper


@optional_debug
def spam(a, b, c):
    print(a, b, c)


spam(1, 2, 3)
spam(1, 2, 3, debug=True)


def a(x, debug=False):
    if debug:
        print('Calling a')
    ...


def b(x, y, z, debug=False):
    if debug:
        print('Calling b')
    ...


def c(x, y, debug=False):
    if debug:
        print('Calling c')
    ...


# 可以将这些代码重构为如下形式:
@optional_debug
def a(x):
    ...


@optional_debug
def b(x, y, z):
    ...


@optional_debug
def c(x, y):
    ...
