Ans = []

def common_element(list_a, list_b):
    common_list = [value for value in list_a if value in list_b]

    if len(common_list) == 1:
        return common_list[0]
    return False

for i in range(10, 100):
    for j in range(i + 1, 100): # denom must be > num
        n_digits = sorted([i//10, i%10])
        d_digits = sorted([j//10, j%10])
        common = common_element(n_digits, d_digits)
        if common:
            n_digits.remove(common)
            d_digits.remove(common)
            n_rem = n_digits[0]
            d_rem = d_digits[0]
            if n_rem != 0 and d_rem != 0:
                if float(i) / j == float(n_rem) / d_rem:
                    Ans.append([i, j])        
product = [1, 1]
for frac in Ans:
    product[0] *= frac[0]
    product[1] *= frac[1]

ans = product[1] / product[0]
print(ans)
