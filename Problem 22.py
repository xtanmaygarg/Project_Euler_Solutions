"""
Input Data From 22.txt in the Given Directory
"""
s = list(input().split(","))
lis = []
for i in s:
    j = list(i)
    j.remove('"')
    j.remove('"')
    lis.append(j)
lis2 = sorted(lis)
dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
l = len(s)
sums = 0
for i in range(l):
    count = 0
    product = i+1
    for j in lis2[i]:
        count += dic[j]
    product *= count
    sums += product
print(sums)
