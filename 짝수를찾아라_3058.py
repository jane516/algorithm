import sys
T = int(input())
for i in range(T):
    case = sys.stdin.readline().strip().split()
    S = []
    Sum = 0
    for j in range(7):
        if int(case[j]) % 2 == 0:
            S.append(int(case[j]))
    print(sum(S), min(S))
