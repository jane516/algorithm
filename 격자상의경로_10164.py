N, M, K = map(int, input().split())


def Factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


if K == 0:
    print(Factorial(N+M-2) // (Factorial(N-1) * Factorial(M-1)))
else:
    a, b = (K-1) // M + 1, K % M
    if b == 0:
        b = M
    A = Factorial(a + b - 2) // (Factorial(a-1) * Factorial(b-1))
    B = Factorial(N + M - a - b) // (Factorial(N - a) * Factorial(M - b))
    print(A * B)