import sys

N = int(sys.stdin.readline().strip())
board = [[0 for _ in range(3)] for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, sys.stdin.readline().strip().split()))

dp_M = board[0]
dp_m = board[0]

for i in range(1, N):
    a = board[i][0]+max(dp_M[0], dp_M[1])
    b = board[i][1]+max(dp_M[0], dp_M[1], dp_M[2])
    c = board[i][2]+max(dp_M[1], dp_M[2])
    dp_M = [a, b, c]

    d = board[i][0]+min(dp_m[0], dp_m[1])
    e = board[i][1]+min(dp_m[0], dp_m[1], dp_m[2])
    f = board[i][2]+min(dp_m[1], dp_m[2])
    dp_m = [d, e, f]

print(max(dp_M), min(dp_m))
