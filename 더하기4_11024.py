import sys
T = int(input())
for i in range(T):
    case = list(map(int, sys.stdin.readline().strip().split()))
    print(sum(case))
