import sys


def is_prime(n):
    m = int(n ** 0.5) + 1
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, m + 1):
            if n % i == 0:
                return False
        return True


T = int(input())
for i in range(T):
    case = sys.stdin.readline().strip()
    n = int(case)
    if n == 0:
        print(2)
    else:
        for j in range(n, 2 * n + 1):
            if is_prime(j):
                print(j)
                break