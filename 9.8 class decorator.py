from functools import wraps


class A:

    # 装饰器作为实例方法
    def decorator1(self, func):
        @wraps(func)
        def wrap(*args, **kwargs):
            print('decorator 1')
            result = func(*args, **kwargs)
            return result

        return wrap

    # 装饰器作为类方法
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorator 2')
            return func(*args, **kwargs)

        return wrapper


a = A()
@a.decorator1
def spam():
    pass


@A.decorator2
def bar():
    pass
