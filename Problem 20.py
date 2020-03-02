from functools import reduce

print(reduce(int.__add__, map(int, str(reduce(int.__mul__, map(int, range(1, 100)))))))
