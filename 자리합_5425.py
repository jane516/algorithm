import sys


def 자리합(N):
    a = list(str(N))
    result = 0
    for i in range(len(a)):
        result += int(a[i])
    return result


T = int(input())
for i in range(T):
    Sum = 0
    case = sys.stdin.readline().strip()
    a = case.split()[0]
    b = case.split()[1]
    for j in range(int(a), int(b) + 1):
        Sum += 자리합(j)
    print(Sum)