Max = 0
Ans = 0
for perimeter in range(10, 1001):
    Curr = 0
    for side1 in range(3, perimeter):
        if ((perimeter ** 2) + (2 * perimeter * side1)) % (2 * perimeter - 2 * side1) == 0:
            Curr += 1
    
    if Max < Curr:
        Max = Curr
        Ans = perimeter
print(Ans)
