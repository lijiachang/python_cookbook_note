from itertools import combinations_with_replacement

items = ['a', 'b', 'c']

for p in combinations_with_replacement(items, 3):
    print(p)

