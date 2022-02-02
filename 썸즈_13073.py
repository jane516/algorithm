t = int(input())
for i in range(t):
    N = int(input())
    S1 = N * (N + 1) // 2
    S2 = N * (N + 1) - N
    S3 = N * (N + 1)
    print(S1, S2, S3)