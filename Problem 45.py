from math import floor
from itertools import count

def quadratic(a, b, c):
    return (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)


def solution():
    for x in count(start=286, step=1):
        t = (x * x + x) // 2
        p = quadratic(3, -1, -2 * t)
        h = quadratic(2, -1, -1 * t)

        if floor(p) == p and floor(h) == h:
            return t

if __name__ == '__main__':
    print(solution())
