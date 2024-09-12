from collections import namedtuple

Stock = namedtuple('Stock', 'name shares price')

s = Stock('AC', 100, 123.45)
print(id(s))
s = s._replace(shares=200)  # _replace()方法生成一个新的对象
print(id(s))
print(s)

# 创建一个原型（模板）
stock_prototype = Stock('', 0, 0)


def dict_to_stock(s: dict):
    """替换原型的默认数据"""
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'price': 10.08}
print(dict_to_stock(a))
