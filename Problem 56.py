Max = 0
for i in range(50, 101):
        for j in range(50, 101):
                Num = i ** j
                Str = sum(list(map(int, str(Num))))
                Max = max(Str, Max)
print(Max)
