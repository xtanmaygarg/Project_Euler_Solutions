lis = []
s = 0
for i in range(1,1000):
    s += i
    lis.append(s)
lis.reverse()
print(lis)
for number in lis:
    d = 1
    for i in range(1, int(number/2)+1):
        if number % i == 0:
            d += 1
            if d > 500:
                print("FOUND AT ", number)    
