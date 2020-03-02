import math as mt
MAXN = 200001
  
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
# calling getFactorization function
A = []
for i in range(1, 150000):
    p = getFactorization(i)
    q = set(p)
    if len(q) == 4 and len(set(getFactorization(i+1))) == 4 and len(set(getFactorization(i+2))) == 4 and len(set(getFactorization(i+3))) == 4:
        print(i)
