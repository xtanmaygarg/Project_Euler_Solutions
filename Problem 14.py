def PE(lim):
    d={}
    a=0
    b=0
    d=[0]*(lim+1)
    d[1]=1
    def rec(n):
        if n==1: return 1
        if n<=lim:
            if d[n]>0:
                return d[n]
        ans = 1 + rec(n//2) if n%2==0 else 1 + rec(3*n+1)
        if n<=lim: d[n]=ans
        return ans
    
    for n in range(1,lim):
        if rec(n)>b: b=rec(n);a=n
    return a
limit = 1000000
print(PE(limit))
