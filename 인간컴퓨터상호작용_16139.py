import sys
S = sys.stdin.readline().strip()
q = int(input())
my_list = [[0 for _ in range(len(S) + 1)] for _ in range(26)]
for i in range(len(S)):
    my_list[ord(S[i]) - ord('a')][i+1] = 1
for i in range(26):
    for j in range(1, len(S) + 1):
        my_list[i][j] += my_list[i][j-1]
for i in range(q):
    case = sys.stdin.readline().strip().split()
    alpha, l, r = case[0], int(case[1]), int(case[2])
    print(my_list[ord(alpha) - ord('a')][r + 1] - my_list[ord(alpha) - ord('a')][l])

