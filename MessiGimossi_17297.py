import sys

dic = {0: 0, 1: 1}
for i in range(2, 41):
    dic[i] = dic[i-1] + dic[i-2]

M = int(sys.stdin.readline().strip())

dp = [0 for _ in range(40)]
for i in range(40):
    dp[i] = dic[i] * 8 + dic[i + 1] * 6 - 1


def messi(N, M):
    if N == 1:
        return M
    if 1 <= M <= dp[N - 1]:
        return messi(N - 1, M)
    elif M == dp[N - 1] + 1:
        return 0
    else:
        M -= dp[N - 1] + 1
        return messi(N - 1, M)


str = 'Messi Gimossi Messi'

result = messi(40, M)
if result == 0 or result == 6:
    print('Messi Messi Gimossi')
else:
    print(str[result - 1])

