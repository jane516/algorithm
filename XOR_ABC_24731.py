import sys
K = int(sys.stdin.readline().strip())


def power(a, n):
    if n == 1:
        return a
    else:
        b = power(a, n // 2)
        if n % 2 == 0:
            return b * b % 1000003
        else:
            return a * b * b % 1000003


X = power(2, K)

result = (X - 1) * (X - 2) * power(6, 1000001) % 1000003
print(result)
