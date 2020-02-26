def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

for i in range(1000,10000):
    if isPrime(i):
        for j in range(i+1,10000):
            if isPrime(j) and set(list(str(i))) == set(list(str(j))):
                for k in range(j+1,10000):
                    if isPrime(k) and set(list(str(i))) == set(list(str(k))):
                        if j == (i + k)//2:
                            print(i,j,k)
            
