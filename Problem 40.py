number = 100
d = ""
for i in range(1,1000000):
    d += str(i)
val = int(d[0]) * int(d[9]) * int(d[99]) * int(d[999]) * int(d[9999]) * int(d[99999]) * int(d[999999])
print(val)
