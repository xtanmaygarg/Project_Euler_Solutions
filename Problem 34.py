import math

def findsum(n):
    smallsum = 0
    while(n>0):
        smallsum = smallsum + math.factorial(n%10)
        n = n//10
    return(smallsum)    

tot = 0
for i in range(10,50000):
    if findsum(i)==i:
        tot = tot + i
print(tot)
