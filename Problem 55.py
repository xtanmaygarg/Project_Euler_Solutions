Count = 0
for i in range(196, 10000):
    S = str(i)
    S = str(int(S) + int(S[:: -1]))
    Iter = 0
    while(S != S[:: -1] and Iter < 51):
        S = str(int(S) + int(S[:: -1]))
        Iter += 1
    if Iter == 51:
        Count += 1
print(Count)
