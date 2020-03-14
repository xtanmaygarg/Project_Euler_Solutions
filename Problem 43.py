def Fundo(n,l):
    if l>len(str(n)):
        return '0'*(l-len(str(n)))+n
    return n

def Finder(n1,n2,pos):
    a=len(n1)-pos
    b=len(n2)-1
    while a>=0 and b>=0:
        if n1[a] != n2[b]: return 0
        a-=1
        b-=1
    return 1

def Solver(n):
    arr=[]
    while n:
        if n[0] in arr: return 1
        arr.append(n[0])
        n=n[1:]
    return 0

arr=[]
i=1

while 17*i<1000:
    if not Solver(Fundo(str(17*i),3)):
        arr.append(Fundo(str(17*i),3))    
    i+=1

i=1
for n in [13,11,7,5,3,2]:
    arr_2=[]
    i=1
    while n*i<1000:
        t=Fundo(str(n*i),3)
        for num in arr:
            if not Solver(t[:-2]+num) and Finder(num,t,len(num)-1):
                arr_2.append(t[:-2]+num)
        i+=1
    arr=arr_2

Ans = []
for i in arr:
    if '1' not in i:
        Ans.append('1' + i)
    elif '4' not in i:
        Ans.append('4' + i)
Ans = map(int, Ans)
del arr
print(sum(Ans))
