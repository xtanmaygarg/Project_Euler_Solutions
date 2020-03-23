from collections import Counter

def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    return prime

if __name__=='__main__': 
    n = 1000000
    Ans = SieveOfEratosthenes(n)
    cumulativeSum = [2]
    X = 0
    for i in range(3, 1000001):
        if Ans[i]:
            cumulativeSum.append(cumulativeSum[X] + i)
            X += 1
    NP = 0
    for i in range(NP, X - 1):
        for j in range(i - NP - 1, -1, -1):
            if cumulativeSum[i] - cumulativeSum[j] > 1000000:
                break
            if Ans[cumulativeSum[i] - cumulativeSum[j]]:
                NP = i - j
                Result = cumulativeSum[i] - cumulativeSum[j]
    print(NP)
    print(Result)

    
