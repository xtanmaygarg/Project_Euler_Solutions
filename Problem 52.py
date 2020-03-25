"""
Number Will Start From 1 Otherwise 6 * Num
Will Increase The Digit

It Will End With 7 As
Only All Multiples of 7 Have Distinct Value:
7 4 1 8 5 2

So Number Will Contain "741852"

Now We Know It Start From 1 End With 7
Hence Number is Of Form:

1----7
"""
from itertools import permutations
Ans = []
for i in permutations('2458', 4):
    X = str(int('1' + ''.join(i) + '7'))
    A = str(int(X) * 2)
    B = str(int(X) * 3)
    C = str(int(X) * 4)
    D = str(int(X) * 5)
    E = str(int(X) * 6)
    if set(A) == set(B) and set(C) == set(D) and set(E) == set(X) and set(X) == set(A):
        Ans.append(X)
print(min(Ans))
    
