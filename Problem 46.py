import math as mt
MAXN = 1000001
  
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
                    
def krdo(x): 
    ret = list() 
    while (x != 1): 
        ret.append(spf[x]) 
        x = x // spf[x] 
  
    return ret

sieve() 
# calling getFactorization function
A = []
XX = {}
for i in range(3, 100000):
    if len(krdo(i)) == 1:
        A.append(i)
        XX[i] = True

for i in range(1, 100000, 2):
    Done = True
    try:
        if XX[i]:
            continue
    except Exception:
        for j in A:
            if j >= i:
                break
            else:
                X = ((i - j)//2)**0.5
                if int(X) == X:
                    Done = True
                    break
                else:
                    Done = False
        if not Done:
            print(i)
            break
                
            
