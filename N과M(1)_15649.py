import sys

N, M = map(int, sys.stdin.readline().strip().split())

check = [0 for _ in range(N + 1)]


def DFS(nums):
    if len(nums) == M:
        print(*nums)
        return

    for i in range(1, N + 1):
        if not check[i]:
            check[i] = 1
            DFS(nums + [i])
            check[i] = 0

DFS([])