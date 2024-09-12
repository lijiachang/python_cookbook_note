# from collections import Iterable  # python 3.10开始弃用，3.3开始警告
from collections import abc


def flatten(items, ignore_types=(str, bytes)):
    """扁平化处理嵌套结构，使用递归。
    flatten: 使...平坦"""
    for x in items:
        if isinstance(x, abc.Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)
