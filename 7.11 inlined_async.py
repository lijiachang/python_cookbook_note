from queue import Queue
from functools import wraps


def apply_async(func, args, *, callback):
    # 计算结果
    result = func(*args)

    # 在回调函数中携带结果
    callback(result)


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break

    return wrapper


# 通过yield语句将回调函数变为内联式
def add(x, y):
    return x + y


@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)

    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)

    print('goodbye')


# test()

if __name__ == '__main__':
    import multiprocessing
    pool = multiprocessing.Pool()
    apply_async= pool.apply_async

    test()