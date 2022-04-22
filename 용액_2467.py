import sys
N = int(sys.stdin.readline().strip())
my_list = list(map(int, sys.stdin.readline().strip().split()))
left, right = 0, N - 1
a, b = my_list[0], my_list[N-1]
m = 2 * 10**9
while left < right:
    Sum = my_list[left] + my_list[right]
    if abs(Sum) < m:
        m = abs(Sum)
        a, b = my_list[left], my_list[right]
    if Sum < 0:
        left += 1
    else:
        right -= 1
print(a, b)
