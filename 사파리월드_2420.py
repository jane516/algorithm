import sys
a, b = map(int, sys.stdin.readline().strip().split())
a, b = max(a, b), min(a, b)
print(a - b)