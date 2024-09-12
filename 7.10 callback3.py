def apply_async(func, args, *, callback):
    # 计算结果
    result = func(*args)
    # 带着结果调用回调函数
    callback(result)


# func
def add(x, y):
    return x + y


# callback
def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print(f'[{sequence}] got:{result}')

    return handler


handler = make_handler()
apply_async(add, (2, 3), callback=handler)
apply_async(add, ('hello', 'world'), callback=handler)
