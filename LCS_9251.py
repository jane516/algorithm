str1 = list(input())
str2 = list(input())
DP = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
for i in range(1, len(str2)+1):
    for j in range(1, len(str1)+1):
        if str2[i-1] == str1[j-1]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])

print(DP[-1][-1])