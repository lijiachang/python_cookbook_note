from functools import wraps
import inspect


def optional_debug(func):
    # 检查参数冲突
    if 'debug' in inspect.getfullargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    # 补充签名
    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter(  # 构造一个参数对象，添加到函数参数签名中
        'debug',
        inspect.Parameter.KEYWORD_ONLY,
        default=False
    ))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper


@optional_debug
def add(x, y):
    return x + y


print(inspect.signature(add))

print(add(2, 3))
