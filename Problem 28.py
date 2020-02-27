Ans = 1
Term = 2
Main = 1
for i in range(3, 1002, 2):
    for j in range(4):
        Main += Term
        Ans += Main
    Term += 2
print(Ans)
    
