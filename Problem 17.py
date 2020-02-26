dic1 = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6}
dic2 = {100:7, 200:7, 300:7, 400:7, 500:7, 600:7, 700:7, 800:7, 900:7}
s = 0
for i in range(1,1001):
    if i < 21:
        s += dic1[i]
    elif i < 100:
        if i in dic1.keys():
            s += dic1[i]
        else:
            d = i % 10
            i = i - d
            s += dic1[i] + dic1[d]
    elif i < 1000:
        if i in dic2.keys():
            s += dic2[i]
            e = i % 100
            i = i - e
            i = i//100
            s += dic1[i]
        else:
            e = i % 100
            i = i - e
            i = i//100
            s += dic1[i] + 10
            if e in dic1.keys():
                s += dic1[e]
            else:
                d = e % 10
                e = e - d
                s += dic1[e] + dic1[d]
    else:
        s += 11
print(s)
