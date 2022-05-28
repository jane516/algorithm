import sys
N, M, K = map(int, sys.stdin.readline().strip().split())
n = K // M
m = K % M
print(n, m)