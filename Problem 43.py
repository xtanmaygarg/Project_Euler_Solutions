sums = 0
for i in range(1023456789,10000000000):
    j = str(i)
    if len(set(list(str(i)))) == 10 and int(j[7:10])%17 == 0 and int(j[6:9])%13 == 0 and int(j[5:8])%11 == 0:
        print(i)
        if int(j[1:4])%2 == 0 and int(j[2:5])%3 == 0:
            if int(j[3:6])%5 == 0 and int(j[4:7])%7 == 0:
                    sums += i
print(sums)
