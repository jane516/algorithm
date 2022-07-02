import sys
T = int(input())
for _ in range(T):
    s = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        q, p = map(int, sys.stdin.readline().strip().split())
        s += q * p
    print(s)