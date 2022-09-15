import sys

N, K = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))
ans = -1


def merge_sort(arr, i, j):
    if i < j:
        m = (i+j) // 2
        merge_sort(arr, i, m)
        merge_sort(arr, m+1, j)
        merge(arr, i, m+1, j)


def merge(arr, i, m, j):
    global K
    global ans
    p = i
    q = m
    r = 0
    temp = [0] * (j-i+1)
    while p < m and q <= j:
        K -= 1
        if arr[p] > arr[q]:
            temp[r] = arr[q]
            q += 1
        else:
            temp[r] = arr[p]
            p += 1
        if K == 0:
            ans = temp[r]
        r += 1

    while p < m:
        temp[r] = arr[p]
        K -= 1
        if K == 0:
            ans = temp[r]
        p += 1
        r += 1

    while q <= j:
        temp[r] = arr[q]
        K -= 1
        if K == 0:
            ans = temp[r]
        q += 1
        r += 1

    p = i
    i = 0
    while p <= j:
        arr[p] = temp[i]
        p += 1
        i += 1


merge_sort(A, 0, N-1)
print(ans)