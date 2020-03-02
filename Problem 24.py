def factorial(n):
    return 1 if n < 1 else n * factorial(n - 1)


def problem24(element):
    from string import digits
    answer = ''
    nums = list(digits)
    while len(nums) != 0:
        factor_num = factorial(len(nums) - 1)
        order = element//factor_num
        if element % factor_num != 0:
            order = element//factor_num + 1
        order %= len(nums)
        answer += nums.pop(order - 1)

    return answer

print(problem24(10 ** 6))
