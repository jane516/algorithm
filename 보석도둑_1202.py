import sys
N, K = map(int, input().split())
VM_list = [[0 for _ in range(2)] for _ in range(N)]
C_list = [[0 for _ in range(2)] for _ in range(K)]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    VM_list = int(case[1]), int(case[0])
for i in range(K):
    C_list[i][0] = int(sys.stdin.readline().strip())

VM_list.sort()
result = 0
for i in range(N):
    V, M = VM_list.pop()