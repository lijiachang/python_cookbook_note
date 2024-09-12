def dedupe(items):
    """去除序列的重复项（序列元素必须是可散列的）"""
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


l = [1, 2, 3, 4, 5, 5, 5, 1, 2, 3]
print(list(dedupe(l)))


def dedupe(items, key=None):
    """去除序列的重复项"""
    seen = set()
    for item in items:
        val = item if key is None else key(item)  # 根据key的规则，转换为可散列的对象val
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

# 按照字典的某个键的值去重
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))

print(list(dedupe(a, key=lambda d: d['x'])))
