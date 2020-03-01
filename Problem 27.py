def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,int(n**0.5+1)):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = []
    for i in range(n):
        if is_prime[i] == True:
            prime.append(i)
    return prime

def is_prime(n):
    for i in range(2,int(abs(n)**0.5)+1):
        if n%i == 0:
            return False
    return True

thousandPrimes = sieve(1000)
primes = thousandPrimes[:]

largest = 0

for b in thousandPrimes:
    for a in thousandPrimes:
        i = 0
        while True:
            quadratic = i**2+a*i+b
            if quadratic not in primes:
                if is_prime(quadratic):
                    primes.append(quadratic)
                else:
                    if i-1 > largest:
                        largest = i-1
                        axb = a*b
                    break
            i += 1
        i = 0
        while True:
            quadratic = i**2-a*i+b
            if quadratic not in primes:
                if is_prime(quadratic) and quadratic>0:
                    primes.append(quadratic)
                else:
                    if i-1 > largest:
                        largest = i-1
                        axb = -1*a*b
                    break
            i += 1
print(axb)
