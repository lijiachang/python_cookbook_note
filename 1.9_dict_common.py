a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# 找出两个字典 相同键
print(a.keys() & b.keys())

# 找出在a，不在b的键
print(a.keys() - b.keys())

# 找出 两个字典相同的键值对
print(a.items() & b.items())

# 修改或过滤掉字典中的内容
# 如去掉字典中的某些键: 过滤掉键为z和w
print({key: a[key] for key in a.keys() - {'z', 'w'}})
