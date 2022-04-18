import sys
L = int(input())
state = [0 for _ in range(L + 1)]
n = int(input())
case1 = list(map(int, sys.stdin.readline().strip().split()))
for i in range(n):
    if case1[i] == 1:
        state