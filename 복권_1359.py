def Combination(n, r):
    분자 = 분모 = 1
    for i in range(0, r):
        분자 = 분자 * (n - i)
        분모 = 분모 * (r - i)
    return 분자 // 분모


N, M, K = map(int, input().split())
Sum = 0
if N <= 2 * M - K:
    print(1.0)
else:
    for i in range(0, M - K + 1):
        Sum += Combination(N - M, M - K - i) * Combination(M, K + i) / Combination(N, M)
    print(Sum)