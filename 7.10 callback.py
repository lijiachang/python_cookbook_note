def apply_async(func, args, *, callback):
    # 计算结果
    result = func(*args)
    # 带着结果调用回调函数
    callback(result)


# callback
def print_result(result):
    print('got:', result)


# func
def add(x, y):
    return x + y


apply_async(add, (2, 3), callback=print_result)
apply_async(add, ('hello', 'world'), callback=print_result)
