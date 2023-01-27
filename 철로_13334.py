import sys

n = int(sys.stdin.readline().strip())
locate = [(0, 0) for _ in range(n)]

for i in range(n):
    l = list(map(int, sys.stdin.readline().strip().split()))
    locate[i] = l[0], l[1]

d = int(sys.stdin.readline().strip())

locate.sort()

start, end = locate[0][0], locate[-1][1]
length = end - start

