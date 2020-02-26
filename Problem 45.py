lis = []
lis2 = []
lis3 = []
for i in range(1, 100000):
    num = (i*(3*i - 1))//2
    lis.append(num)
    num2 = (i*(i + 1))//2
    lis2.append(num2)
    num3 = (i*(2*i - 1))
    lis3.append(num3)
for i in lis:
    if i in lis2 and i in lis3:
        print(i)
