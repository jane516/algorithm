import sys
N = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().strip().split()))
k = int(sys.stdin.readline().strip())
count = 0


def dfs(n, arr):
    arr[n] = -2
    for i in range(len(arr)):
        if n == arr[i]:
            dfs(i, arr)


dfs(k, num)
for i in range(len(num)):
    if num[i] != -2 and i not in num:
        count += 1
print(count)