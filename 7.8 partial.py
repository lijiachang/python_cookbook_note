import math
import functools

points = [(1, 2), (3, 4), (5, 6), (7, 8)]


def distance(p1, p2):
    """计算两点之间的距离"""
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


pt = (4, 3)
points.sort(key=functools.partial(distance, pt))
print(points)