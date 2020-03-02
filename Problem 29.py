nums_distinct = []
for x in range(2, 101):
    for y in range(2, 101):
        num = x ** y
        if num not in nums_distinct:
            nums_distinct.append(num)

print(len(nums_distinct))

