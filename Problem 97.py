def Power(N, P, M):
    Result = 1
    while(P > 0):
        if P & 1:
            Result *= N
            Result %= M

        N *= N
        N %= M
        P = P >> 1
    return Result

N = 2
M = 10000000000
P = 7830457
SubAnswer = Power(N, P, M)
print((28433 * SubAnswer + 1) % M)

