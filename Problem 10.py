import math as mt
MAXN = 2000001

spf = [0 for i in range(MAXN)]  
def sieve(): 
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i
        
    for i in range(4, MAXN, 2): 
        spf[i] = 2
  
    for i in range(3, mt.ceil(mt.sqrt(MAXN))): 
        if (spf[i] == i): 
            for j in range(i * i, MAXN, i):  
                if (spf[j] == j): 
                    spf[j] = i
                    
def getFactorization(x): 
    ret = list() 
    while (x != 1): 
        ret.append(spf[x]) 
        x = x // spf[x] 
  
    return ret

sieve() 
answer = 0
for i in range(2, 2000001):
    p = getFactorization(i)
    if len(p) == 1:
        answer += i
print(answer)
