from math import factorial

def NCR(Val, Point):
        return factorial(Val) // (factorial(Val - Point) * factorial(Point))

Ans = 4
Point = 10
for Val in range(24, 101):
        if NCR(Val, Point - 1) > 1000000:
                Point -= 1
        Ans += Val - 2 * Point + 1
print(Ans)
