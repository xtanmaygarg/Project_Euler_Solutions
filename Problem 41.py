from collections import Counter
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    return prime, len(prime)

if __name__=='__main__': 
    n = 7654322
    Ans, L = SieveOfEratosthenes(n)
    for i in range(L - 1, -1, -1):
        if Ans[i] and set(Counter(str(i)).keys()) == set('1234567'):
            print(i)
            break
