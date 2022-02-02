def Combination(n, r):
    분자 = 분모 = 1
    if r > n-r:
        r = n-r
    for i in range(0, r):
        분자 = 분자 * (n - i)
        분모 = 분모 * (r - i)
    return 분자 // 분모


N, K = map(int, input().split())
if N < K - 1:
    print(Combination(N+K-1, N) % 1000000000)
else:
    print(Combination(N + K - 1, K-1) % 1000000000)