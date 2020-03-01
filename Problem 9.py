def decompSum(n):
    from itertools import combinations
    m = (x for x in range(1, n // 2))
    div = [3, 4, 5]
    comb = combinations((x for x in m if any(d for d in div if not x % d)), 3)
    for a, b, c in comb:
        if a + b + c == n and a != b != c:
            yield sorted((a, b, c))


def pythagorean(a, b, c):
    return (a ** 2 + b ** 2) == c ** 2


def problem9(n):
    for a, b, c in decompSum(n):
        if pythagorean(a, b, c):
            return a * b * c


print(problem9(1000))
