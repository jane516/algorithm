import sys
T = int(input())
for k in range(T):
    case = sys.stdin.readline().strip().split()
    L = int(case[0])
    U = int(case[1])
    result = 0
    for i in range(int(L), int(U) + 1):
        for j in list(str(i)):
            result += int(j)
    print(result)