from collections.abc import Sequence
import bisect


class SortedItems(Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, item):
        return self._items[item]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)  # 有序的插入序列，如果重复，就插入右侧


items = SortedItems([5, 1, 3])
print(list(items))

items.add(2)
print(list(items))

print(3 in items)
print(items[-1])

import collections
items = SortedItems()

print(isinstance(items, collections.Iterable))
print(isinstance(items, collections.Sequence))
print(isinstance(items, collections.Container))
print(isinstance(items, collections.Sized))
print(isinstance(items, collections.Mapping))