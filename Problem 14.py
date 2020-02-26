def seq(n):
    count = 0
    while(n != 1):
        count += 1
        if n%2 == 0:
             n = n//2
        else:
            n = 3*n + 1
    count += 1
    return count
for i in range(100000,1000000):
    ma = 0
    term = 0
    if seq(i) > ma:
        ma = seq(i)
        term = i
print(term)
