N = int(input())
S = [0] * N
for j in range(N):
    S[j] = int(input())
DP = [0] * (N + 1)

if N == 1:
    print(S[0])
elif N == 2:
    print(S[0] + S[1])
else:
    DP[1] = S[0]
    DP[2] = S[0] + S[1]

    for i in range(3, N + 1):
        DP[i] = max(DP[i-2], DP[i-3] + S[i-2]) + S[i-1]
    print(DP[N])