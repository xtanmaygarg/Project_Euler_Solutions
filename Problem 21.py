def div(n):
    su = 0
    for i in range(1,n):
        if n%i == 0:
            su += i
    return su
s = 0
for i in range(1,10001):
    num = div(i)
    if div(num) == i and i != num:
        s += i
print(s)
