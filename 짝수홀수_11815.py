import sys
N = int(input())
case = sys.stdin.readline().strip().split()
A = []
for i in range(N):
    if int(int(case[i]) ** 0.5) ** 2 == int(case[i]):
        A.append(1)
    else:
        A.append(0)
for j in range(N):
    print(A[j], end=' ')