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


N, K = map(int, input().split())
R = Factorial(N) * power(Factorial(K) * Factorial(N - K), 1000000005) % 1000000007
print(R)