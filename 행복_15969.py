import sys

N = int(input())
A = []
case = sys.stdin.readline().strip()
for i in range(N):
    A.append(int(case.split()[i]))
print(max(A) - min(A))
