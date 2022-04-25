import sys
N = int(input())
A_list = list(map(int, sys.stdin.readline().strip().split()))
A_list.sort()
X, Y = map(int, input().split())
result1 = N * X // 100
count = 0
for i in range(N):
    if A_list[i] >= Y:
        count += 1
print(result1, count)