import sys
case = sys.stdin.readline().strip().split()
N, K = int(case[0]), int(case[1])
A = list(map(int, sys.stdin.readline().strip().split()))
cnt, Sum, dic = 0, 0, {0: 1}
for i in range(N):
    Sum += A[i]
    if Sum - K in dic:
        cnt += dic[Sum - K]
    if Sum in dic:
        dic[Sum] += 1
    else:
        dic[Sum] = 1
print(cnt)