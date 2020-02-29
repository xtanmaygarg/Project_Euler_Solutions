from timeit import default_timer as timer
start = timer()
import math as mt
MAXN = 30000

def factors(Back, Term):
    Ans = {1}
    for i in Back:
        New = set()
        for j in Ans:
            New.add(i*j)
        Ans = Ans.union(New)
    Ans.remove(Term)
    Sum = sum(Ans)
    if Sum > Term:
        return Sum
    else:
        return False
 
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
A = {}
for i in range(1, 28123):
    p = getFactorization(i)
    R = factors(p, i)
    if R:
        A[i] = R
Answer = 0
Keys = sorted(list(A.keys()))
for i in range(1, 28123):
    flag = True
    for j in Keys:
        if j > i:
            if flag:
                Answer += i
                break
            else:
                break
        try:
            if A[i - j]:
                break
        except Exception:
            pass
print(Answer)
print(timer() - start)
