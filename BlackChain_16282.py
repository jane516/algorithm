import sys
n = int(sys.stdin.readline().strip())
k = 1


def pow(k, n):
    if n == 1:
        return k
    else:
        A = pow(k, n // 2)
        if n % 2 == 0:
            return A * A
        else:
            return A * A * k


while True:
    if n >= k * pow(2, k) - 1 and n <= (k + 1) * pow(2, k + 1) - 1:
        break
    else:
        k += 1
print(k)