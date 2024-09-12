words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under']

from collections import Counter

word_counters = Counter(words)
print(word_counters.most_common(3))  # 找出元素数量最多的三个元素
print(word_counters['eyes'])  # 在底层实现中，Counter其实是一个字典，是dict的子类。是对元素和它出现的次数做了映射

# 想要手动增加次数，只需要自增即可
more_words = 'in my eyes'.split()
for word in more_words:
    word_counters[word] += 1
print(word_counters['eyes'])
# 或者使用update方法
word_counters.update(more_words)

# 另外，Counter对象还能使用各种数学运算操作
print(Counter(words) - Counter(more_words))
print(Counter(words) + Counter(more_words))