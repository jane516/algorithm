N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
dp = [1] * N
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))