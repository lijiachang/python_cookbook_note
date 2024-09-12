from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper


@decorator
def add(x, y):
    return x + y


orig_add = add.__wrapped__  # 获取原始函数
print(orig_add(1, 2))
