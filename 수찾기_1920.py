import sys

N = int(input())
a_list = list(map(int, sys.stdin.readline().strip().split()))

M = int(input())
m_list = list(map(int, sys.stdin.readline().strip().split()))

dic = {}

for i in range(N):
    dic[a_list[i]] = 1

for j in range(M):
    if m_list[j] in dic:
        print(1)
    else:
        print(0)