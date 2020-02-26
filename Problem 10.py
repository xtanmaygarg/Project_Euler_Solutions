answer = 0
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for i in range(2,2000000):
    prime = isPrime(i)
    if(prime == True):
        answer += i    


print(answer)
