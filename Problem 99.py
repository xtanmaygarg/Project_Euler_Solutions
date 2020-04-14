from math import log
List = []
for i in range(1000):
    List.append(list(map(int, input().split(','))))

Max = 0
Curr = 0
for i in range(1000):
    Num = log(List[i][0]) * List[i][1]
    if Num > Max:
        Max = Num
        Curr = i + 1
print(Curr)
