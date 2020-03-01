num = 1
longest = 1
for n in range(3, 1000, 2):
    if n % 5 == 0:
        continue

    p = 1
    while (10 ** p) % n != 1:
        p += 1

    if p > longest:
        num, longest = n, p

print(num)
