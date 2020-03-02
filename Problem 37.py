def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
s = 0
k = 1
for i in range(10,1000000):
    if isPrime(i):     
        flag = 0
        j = i
        while(i > 0):
            flag = 1
            i = i//10
            if not isPrime(i):
                flag = 0
                break
        num = 10
        while k > 0 and num < j:
            k = j % num
            num *= 10
            if not isPrime(k):
                flag = 0
                break
        if flag == 1:
            s += j
print(s)
