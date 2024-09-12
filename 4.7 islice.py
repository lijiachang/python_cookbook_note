import itertools


def cont(n):
    while True:
        yield n
        n += 1


c = cont(0)
for x in itertools.islice(c, 10, 20):
    print(x)
