def apply_async(func, args, *, callback):
    # 计算结果
    result = func(*args)
    # 带着结果调用回调函数
    callback(result)


# func
def add(x, y):
    return x + y


# callback
class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print(f'[{self.sequence}] got:{result}')


cb = ResultHandler()
apply_async(add, (2, 3), callback=cb.handler)
apply_async(add, ('hello', 'world'), callback=cb.handler)
