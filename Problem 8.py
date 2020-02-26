for i in range(20,500):
    for j in range(20,500):
        for k in range(20,500):
            if(i+j+k == 1000):
                if(i**2 + j**2 == k**2 or i**2 == j**2 + k**2 or j**2==k**2 + i**2):
                    print(i*j*k)
