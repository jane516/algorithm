import sys
T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    building = [[0 for _ in range(w)] for _ in range(h)]