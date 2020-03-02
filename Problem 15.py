def Problem15(n):
    line = [1]
    lines = 0
    while lines < n:
        i = 0
        newline = [1, 1]
        while len(newline) - 1 <= lines and len(line) - 1 > i:
            new = line[i] + line[i + 1]
            newline.insert(i + 1, new)
            i += 1
        line = newline
        lines += 1

    return line


def solution():
    Hello = Problem15(40)
    middle = len(Hello) // 2
    return Hello[middle]

print(solution())
