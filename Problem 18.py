"""
Please Input:

15
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

lis = []
n = int(input())
for i in range(n):
    lis.append(list(map(int, input().split())))
l = [[lis[0][0]]]
for i in range(1,n):
    l1 = []
    if i == 1:
        j = 0
        l1.append(lis[i][j] + lis[i-1][j])
        l1.append(lis[i][j+1] + lis[i-1][j])
        l.append(l1)
    else:
        for j in range(len(lis[i])):
            if j == 0:
                l1.append(lis[i][j] + l[i-1][j])
            elif j == len(lis[i]) - 1:
                l1.append(lis[i][j] + l[i-1][j-1])
            else:
                l1.append(lis[i][j] + max(l[i-1][j],l[i-1][j-1]))
        l.append(l1)
print(max(l[i]))            
    








"""
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
