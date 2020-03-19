Ans = set()
for i in range(1, 10):
    s = str(i)
    for j in range(1000, 10000):
        s += str(j)
        s += str(j * i)
        if len(s) == 9:
            if set(s) == {'1', '8', '3', '9', '6', '4', '5', '2', '7'}:
                Ans.add(j * i)
        s = str(i)
for i in range(10, 100):
    s = str(i)
    for j in range(100, 1000):
        s += str(j)
        s += str(j * i)
        if len(s) == 9:
            if set(s) == {'1', '8', '3', '9', '6', '4', '5', '2', '7'}:
                Ans.add(j * i)
        s = str(i)

print(sum(Ans))
