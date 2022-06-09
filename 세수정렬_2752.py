import sys
N_list = list(map(int, sys.stdin.readline().strip().split()))
N_list.sort()
print(*N_list)