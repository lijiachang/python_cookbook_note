items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[a])
items[a] = [20, 30]  # 对切片赋值
print(items)
del items[a]  # 删除切片位置的元素
print(items)

s = slice(2, 50, 2)
print(s.start, s.stop, s.step)

items = [0, 1, 2, 3, 4, 5, 6]
s = slice(3, 10, 2)

print(s.indices(len(items)))
print(items[slice(*s.indices(len(items)))])
