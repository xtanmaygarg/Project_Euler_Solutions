maxed = 0
for i in range(901,1000):
    for j in range(901,1000):
        if(str(i*j)[::-1]==str(i*j)):
            if(maxed<i*j):
                maxed = i*j
print(maxed)
            
