import sys
case = sys.stdin.readline().strip().split()
N, r, c = int(case[0]), int(case[1]), int(case[2])
def Z(N, r, c):
    if N == 0:
        return 0
    else:
        return 4 * Z(N - 1, r // 2, c // 2) + 2 * (r % 2) + c % 2
print(Z(N, r, c))