from functools import wraps
from .postimport import when_imported

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return wrapper

@when_imported('math')
def add_logging(mod):
    mod.cos= logged(mod.cos)
    mod.sin = logged(mod.sin)