def apply_async(func, args, *, callback):
    # 计算结果
    result = func(*args)
    # 带着结果调用回调函数
    callback(result)


# func
def add(x, y):
    return x + y


# callback
class SequenceNo:
    def __init__(self):
        self.sequence = 0


def handler(result, seq: SequenceNo):
    seq.sequence += 1
    print(f'[{seq.sequence}] got:{result}')


from functools import partial

sequence_no = SequenceNo()
apply_async(add, (2, 3), callback=partial(handler, seq=sequence_no))
apply_async(add, ('hello', 'world'), callback=partial(handler, seq=sequence_no))
