import heapq

nums = [1, 2, 5, 8, -2, -9, 90, 0, 11]
print(heapq.nlargest(3, nums))  # 最大的三个数
print(heapq.nsmallest(3, nums))  # 最小的三个数

heapq.heapify(nums)  # heapify函数会就地修改序列，以堆的顺序排列
print(nums)

# 要找到第三小的元素
print(heapq.heappop(nums))
print(heapq.heappop(nums))
print(heapq.heappop(nums))

