import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f'{label}: {end - start}')


with timethis('counting'):
    n = 10000000
    while n > 0:
        n -= 1


class timethis:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print(f'{self.label}: {end - self.start}')
