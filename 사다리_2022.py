import sys
from sympy import Symbol, solve
case = sys.stdin.readline().strip().split()
x, y, c = int(case[0]), int(case[1]), int(case[2])
k = (x**2 - y**2) / c**2
a = Symbol('a')
equation = k * a ** 2 * (1 - a) ** 2 - 2 * a + 1
solve(equation)
