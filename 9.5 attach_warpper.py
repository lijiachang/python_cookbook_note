from functools import wraps, partial
import logging


def attach_wrapper(obj, func=None):
    """将函数func附加到obj的属性"""
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    def decorate(func):
        log_name = name if name else func.__module__
        log = logging.getLogger(log_name)
        log_msg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, log_msg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper)
        def set_message(new_msg):
            nonlocal log_msg
            log_msg = new_msg

        return wrapper

    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('spam!')


import logging

logging.basicConfig(level=logging.DEBUG)

print(add(2, 3))

add.set_message('add called')  # 修改log的打印
print(add(2, 3))

add.set_level(logging.WARNING)  # 修改log等级
print(add(2, 3))
