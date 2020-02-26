#!/bin/python3
""" Euclidean GCD Algorithm """
def gcd(x,y):
    return x if y==0 else gcd(y,x%y)

""" Using the property lcm*gcd of two numbers = product of them """
def lcm(x,y):
    return (x*y)//gcd(x,y)

n = int(input())
g=1
for i in range(1,n+1):
    g=lcm(g,i)
print(g)
