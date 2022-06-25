import sys
w, n = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))
A.sort()
w_list = [0 for _ in range(w)]
for i in range(n):
    for j in range(i + 1, n):
        if A[i] + A[j] < w and w_list[w - A[i] - A[j]]:
            print('YES')
            exit(0)
    for j in range(i):
        if A[i] + A[j] < w:
            w_list[A[i] + A[j]] = 1
print('NO')