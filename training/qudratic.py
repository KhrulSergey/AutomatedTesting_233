__author__ = 'Sergey Khrul'

from math import sqrt


def solve (a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        return "No solution"
    elif d == 0:
        return "One solution: {}".format(-b / (2 * a))
    elif d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return "Two solutions: {} and {}".format(x1, x2)
    else:
        return "Exception!!"


print(solve(1, 1, 1))
print(solve(1, 2, 1))
print(solve(1, 5, 6))
