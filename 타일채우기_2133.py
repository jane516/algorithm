N = int(input())
DP = [0 for _ in range(16)]

DP[1] = 3
DP[2] = 11
for i in range(3, 16):
    DP[i] += DP[i-1] * 3 + 2
    for j in range(2, i):
        DP[i] += DP[i-j] * 2


if N % 2 == 0:
    print(DP[N//2])
else:
    print(0)