class Proxy:
    """代理类，包裹在其他对象，暴露自己的公共属性"""

    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        """委托属性查找自内部obj"""
        print('getattr:', item)
        return getattr(self._obj, item)

    def __setattr__(self, key, value):
        """委托属性分配"""
        if key.startswith("_"):
            super().__setattr__(key, value)
        else:
            print('setter:', key, value)
            setattr(self._obj, key, value)

    def __delattr__(self, item):
        """委托属性删除"""
        if item.startswith("_"):
            super().__delattr__(item)
        else:
            print('delattr:', item)
            delattr(self._obj, item)


class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar print:', self.x, y)


# 创建一个实例
s = Spam(2)
# 创建一个代理包裹他
p = Proxy(s)

print(p.x)
p.bar(3)
p.x = 44
