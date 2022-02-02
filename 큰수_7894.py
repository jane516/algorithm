import math


def factorial_자리수(n):
    result = 0
    for i in range(1, n + 1):
        result += math.log10(i)
    return result


m = int(input())
for i in range(m):
    n = int(input())
    k = factorial_자리수(n)
    print(int(k) + 1)