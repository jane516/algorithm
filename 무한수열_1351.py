import sys
case = sys.stdin.read().strip().split()
N, P, Q = int(case[0]), int(case[1]), int(case[2])
dp = [0 for _ in range(10**5)]
dp[0] = 1
dp[1] = 2
for i in range(1000):
    n, m = i, i
    while True:
        if n % P < P:
            break
        n //= P
    while True:
        if m % Q < Q:
            break
        m //= Q
    dp[i] = dp[n]
