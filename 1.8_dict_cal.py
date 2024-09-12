# 股票名称和对应的价格：
prices = {'ACME': 45.67,
          'AAPL': 612.34,
          'IBM': 205.33,
          'HPQ': 37.20,
          'FB': 10.75}

# 求最大值和最小值
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price)
print(max_price)

# 对数据排序,从小到大
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
# !!! 要注意的是，zip()创建了一个迭代器，只能被消费一次

# 得到最大值和最小值对应的键
print(min(prices, key=lambda x: prices[x]))
print(max(prices, key=lambda x: prices[x]))

# 想要得到最小值，需要额外的一次查找
print(prices[min(prices, key=lambda x: prices[x])])
