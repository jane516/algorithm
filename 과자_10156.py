import sys
case = sys.stdin.readline().strip().split()
K, N, M = int(case[0]), int(case[1]), int(case[2])
if M >= K * N:
    print(0)
else:
    print(K * N - M)