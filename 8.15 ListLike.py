class ListLike:
    def __init__(self):
        self._items = []

    def __getattr__(self, item):
        return getattr(self._items, item)


a = ListLike()
a.append(2)
a.insert(0, 1)
a.sort()

len(a)
a[0]

