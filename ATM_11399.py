import sys
N = int(input())
case = sys.stdin.readline().strip()
P_list = [0] * N
for i in range(N):
    P_list[i] = int(case.split()[i])
P_list.sort()
for i in range(1, N):
    P_list[i] += P_list[i-1]
print(sum(P_list))