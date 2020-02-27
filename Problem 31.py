Val = 200
D = [1, 2, 5, 10, 20, 50, 100, 200]
DP = []
for i in range(len(D)):
    DP.append([0] * 201)

for i in range(len(D)):
    for j in range(201):    
        if j < D[i]:
            if D[i] == 1:
                continue
            else:
                DP[i][j] = DP[i - 1][j]
        elif D[i] == 1:
            DP[i][j] = 1
        elif D[i] == j:
            DP[i][j] = DP[i - 1][j] + 1
        else:
            DP[i][j] = DP[i - 1][j] + DP[i][j - D[i]]
print(DP[7][200])
