su = 0
for i in range(1, 1000001):
    if i == int(str(i)[::-1]):
        if "{0:b}".format(i)[::-1] == "{0:b}".format(i):
            print(i)
            su += i
print(su)
