def check_abun(n):
    s = 0
    for i in range(1,n//2+1):
        if n % i == 0:
            s += i
    if s > n:
        return True
    return False
l = []
for i in range(1,10000,2):
    if check_abun(i):
        l.append(i)
