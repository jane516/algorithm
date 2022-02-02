import sys
dp = [0] * 51

def Factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i % 1000000007
    return result


def power(a, n):
    if n == 1:
        return a
    else:
        b = power(a, n // 2)
        if n % 2 == 0:
            return b * b % 1000000007
        else:
            return a * b * b % 1000000007


case = sys.stdin.readline().strip().split()
N = int(case[0])
K = int(case[1])
dp[0] = N
for i in range(1, 51):
    dp[i] = (power(N + 1, i + 1) - 1) * power(i + 1, 1000000005) % 1000000007
    for j in range(1, i + 1):
        dp[i] -= Factorial(i + 1) * power(Factorial(j + 1) * Factorial(i - j), 1000000005) * dp[i - j] * power(i + 1, 1000000005) % 1000000007
print(dp[K] % 1000000007)