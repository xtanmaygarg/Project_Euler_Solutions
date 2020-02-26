lis = []
for i in range(1, 801):
    num = (i*(3*i - 1))//2
    lis.append(num)
d = 10000000
for i in lis:
    for j in lis:
        if (i + j) in lis and abs(i - j) in lis:
            if d > abs(i - j):
                d = abs(i - j)
print(d)
