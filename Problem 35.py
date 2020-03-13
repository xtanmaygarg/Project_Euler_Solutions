# Prime Sieve
def SieveOfEratosthenes(n): 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return prime

n = 10000000
prime = SieveOfEratosthenes(n)
Ans = []
count = 1
for i in range(3, 1000001, 2):
    if prime[i]:
        temp = str(i)
        j = temp[-1] + temp[:-1]
        lis = [temp, j]
        while(j != temp):
            j = j[-1] + j[:-1]
            lis.append(j)
        flag = 1
        for kk in lis:
            if not prime[int(kk)]:
                flag = 0
        if flag == 1:
            count += 1
            Ans.append(i)    
print(count)
