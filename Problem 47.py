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
        print(i, p)
        print(i+1)
        print(i+2)
        print(i+3)
"""
import math
import time


def has_exact_n_prime_factor(input_value, n):
    count = 0
    if input_value % 2 == 0:
        count += 1
        while input_value % 2 == 0:
            input_value /= 2
    limit = math.sqrt(input_value)
    prime_number_in_check = 3
    while input_value > 1 and prime_number_in_check <= limit:
        if input_value % prime_number_in_check == 0:
            count += 1
            if count > n:
                break
            while input_value % prime_number_in_check == 0:
                input_value /= prime_number_in_check
            limit = math.sqrt(input_value)
        prime_number_in_check += 2
    if input_value != 1:
        count += 1
    return count == n


if __name__ == '__main__':
    start = time.time()
    result = 0
    no_in_checked = 20
    while True:
        if has_exact_n_prime_factor(no_in_checked, 4):
            for i in range(1, 4):
                if not has_exact_n_prime_factor(no_in_checked+i, 4):
                    no_in_checked += i
                    break
            else:
                result = no_in_checked
                break
        else:
            no_in_checked += 1

    print(result)
    print(time.time() - start)
"""
