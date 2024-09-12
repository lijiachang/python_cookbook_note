import types
from functools import wraps


def profiled(func):
    ncalls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)

    wrapper.ncalls = lambda: ncalls  # 每次调用时都会动态获取 ncalls 的最新值，可以通过 add.ncalls() 获取到 add 函数被调用的次数。
    return wrapper


@profiled
def add(x, y):
    return x + y


print(add(1, 2))
print(add(2, 3))
print(add.ncalls())
