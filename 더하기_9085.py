import sys
T = int(input())
for i in range(T):
    Sum = 0
    N = int(input())
    case = sys.stdin.readline().strip().split()
    for j in range(N):
        Sum += int(case[j])
    print(Sum)