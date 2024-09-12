from itertools import chain

a = {1, 2, 3}
b = {'a', 'b', 'c'}

for x in chain(a, b):
    print(x)
