import sys
import math

N = int(sys.stdin.readline().strip())
A_list = list(map(int, sys.stdin.readline().strip().split()))
B_list = sorted(A_list)
check = 0

for i in range(len(A_list)):
    if math.isqrt(A_list[i] * B_list[i]) ** 2 != A_list[i] * B_list[i]:
        check = 1
        break
    else:
        continue

if check == 0:
    print('YES')
else:
    print('NO')
