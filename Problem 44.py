Pent = []
Penta = {}
for i in range(1, 3002):
    N = (i * (3 * i -  1)) // 2
    Pent.append(N)
    Penta[N] = True
    
Diff = 10e15
for i in range(3001):
    for j in range(i + 1, 3001):
        if Pent[i] + Pent[j] in Penta and abs(Pent[j] - Pent[i]) in Penta:
            Diff = min(Diff, Pent[j] - Pent[i])
print(Diff)
            
