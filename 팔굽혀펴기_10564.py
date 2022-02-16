import sys
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    case = sys.stdin.readline().strip().split()
    score = []
    for j in range(M):
        score.append(int(case[j]))
    DP = [[0 for _ in range(501)] for _ in range(N + 1)]
    for j in score:
        DP[j][j] = j
    for l in range(N + 1):
        for j in range(l + 1):
            if j <= 500:
                for k in score:
                    if j - k >= 0 and DP[l - j][j - k] != 0:
                        DP[l][j] = max(DP[l][j], DP[l - j][j - k] + k)
                    else:
                        continue
    result = max(DP[N])
    if result == 0:
        print(-1)
    else:
        print(result)
