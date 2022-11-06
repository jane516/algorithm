import sys

n = int(sys.stdin.readline().strip())
my_list = list(map(int, sys.stdin.readline().strip().split()))
my_list.sort()
x = int(sys.stdin.readline().strip())

cnt = 0

for start in range(n-1):
    a1 = my_list[start]
    if a1 > x // 2:
        break
    for end in range(start+1, n):
        a2 = my_list[end]
        if a1 + a2 > x:
            break
        if a1 + a2 == x:
            cnt += 1

print(cnt)
