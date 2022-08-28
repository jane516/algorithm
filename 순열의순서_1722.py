import sys

N = int(input())
input = list(map(int, sys.stdin.readline().strip().split()))
order = input[0]
N_fac = 1
for i in range(N - 1):
    N_fac *= (i + 1)
if order == 1:
    nums = [i for i in range(1, N + 1)]
    result = []
    k = input[1]
    for i in range(N - 1):
        num = nums[(k-1) // N_fac]
        result.append(num)
        nums.remove(num)
        k %= N_fac
        N_fac //= (N - 1 - i)
    result.append(nums[0])
    print(*result)
else:
    nums = [i for i in range(1, N + 1)]
    Sum = 0
    for i in range(N - 1):
        num = input[i + 1]
        idx = nums.index(num)
        Sum += idx * N_fac
        nums.remove(num)
        N_fac //= (N - 1 - i)
    print(Sum + 1)
