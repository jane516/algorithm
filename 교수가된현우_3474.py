import sys


def 오의개수(n):
    Sum = 0
    A = 5
    while n // A > 0:
        Sum += n // A
        A *= 5
    return Sum


T = int(input())
for i in range(T):
    N = int(sys.stdin.readline().strip())
    print(오의개수(N))