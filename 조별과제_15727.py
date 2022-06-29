import sys

L = int(sys.stdin.readline().strip())
r = L % 5
if r == 0:
    print(L // 5)
else:
    print(L // 5 + 1)