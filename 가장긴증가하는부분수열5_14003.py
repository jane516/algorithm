from bisect import bisect_left
import sys
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
L = [A[0]]
index_list = [[0, A[0]]]
for i in range(1, N):
    if L[-1] < A[i]:
        L.append(A[i])
        index_list.append([len(L)-1, A[i]])
    else:
        idx = bisect_left(L, A[i])
        L[idx] = A[i]
        index_list.append([idx, A[i]])
print(len(L))
M = len(L) - 1
result = []
k = 0
for i in range(N):
    if M == -1:
        break
    if M == index_list[-1-i][0]:
        result.append(index_list[-1-i][1])
        M -= 1
print(*result[::-1])