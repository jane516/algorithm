N = int(input())
A = list((map(int, input().split())))
Check = 0
for i in range(N-1, 0, -1):
    if A[i-1] < A[i]:
        for j in range(N-1, i, -1):
            if A[i-1] < A[j]:
                Check = 1
                A[i-1], A[j] = A[j], A[i-1]
                break
        if Check == 0:
            A[i - 1], A[i] = A[i], A[i - 1]
        A = A[:i] + sorted(A[i:])
        Check = 1
        break
if Check == 1:
    for k in A:
        print(k, end=' ')
else:
    print(-1)
