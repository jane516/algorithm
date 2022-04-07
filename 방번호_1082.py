import sys
N = int(input())
case = sys.stdin.readline().strip().split()
P_list = [0 for _ in range(N)]
for i in range(N):
    P_list[i] = int(case[i])
M = int(input())
