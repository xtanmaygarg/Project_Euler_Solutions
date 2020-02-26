def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
count = 0
j = 1
for i in range(1,1000):
    if isPrime(i):
        temp = i
        lis = [i]
        while(j != temp) and i > 10:
            d = i % 10
            k = str(i // 10)
            i = int(str(d) + k)
            print(i)
            j = i
            lis.append(j)
        flag = 1
        for kk in lis:
            if not isPrime(kk):
                flag = 0
        if flag == 1:
            count += 1
print(count)
