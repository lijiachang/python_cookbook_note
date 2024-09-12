from contextlib import contextmanager


@contextmanager
def list_transaction(origin_list):
    working = list(origin_list)  # 创建一个副本，避免修改源列表
    yield working
    origin_list[:] = working  # 将 working 中的所有元素复制到 origin_list 所指向的列表中，从而实现了对原始列表的修改。


items = [1, 2, 3, 4, 5]
with list_transaction(items) as working_:
    working_.append(6)
    working_.append(7)
    # raise RuntimeError('oops')  # 如果抛出异常，则不会修改源列表

print(items)
