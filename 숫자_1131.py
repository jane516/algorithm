import sys

A, B, K = map(int, sys.stdin.readline().strip().split())
INF = 9**6 * 6 + 1
dp = [INF for _ in range(1000001)]

def DFS(n):
    if dp[n] == INF:
