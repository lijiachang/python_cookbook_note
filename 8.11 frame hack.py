def init_from_locals(self):
    """将当前的变量添加到实例属性中"""
    import sys
    locals = sys._getframe(1).f_locals
    for k, v in locals.items():
        print(k, v)  # 打印下locals都有什么
        if k != 'self':
            setattr(self, k, v)


class Stock:
    def __init__(self, name, shares, price):
        init_from_locals(self)


s = Stock('li', shares=12, price=88)
print(s.name)
