from bisect import bisect_left
import sys
N = int(sys.stdin.readline().strip())
link = [[0 for _ in range(2)] for _ in range(N)]
for i in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    link[i] = a, b
link.sort()
A = [link[i][1] for i in range(N)]
L = [A[0]]
dic = {}
index_list = [[0, A[0]]]
for i in range(1, N):
    if L[-1] < A[i]:
        L.append(A[i])
        index_list.append([len(L)-1, A[i]])
    else:
        idx = bisect_left(L, A[i])
        L[idx] = A[i]
        index_list.append([idx, A[i]])
print(N - len(L))
M = len(L) - 1
result = []
k = 0
for i in range(N):
    if M == -1:
        break
    if M == index_list[-1-i][0]:
        result.append(index_list[-1-i][1])
        M -= 1
B = list(set(A) - set(result))
C = []
for i in range(N):
    if link[i][1] in B:
        C.append(link[i][0])
C.sort()
for i in range(len(C)):
    print(C[i])