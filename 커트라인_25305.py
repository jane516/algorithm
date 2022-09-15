import sys

N, k = map(int, sys.stdin.readline().strip().split())
score = list(map(int, sys.stdin.readline().strip().split()))
print(sorted(score)[N - k])