M = int(input())
N = int(input())
m = int(M ** 0.5)
n = int(N ** 0.5)
A = []
if m ** 2 != M:
    m = m + 1
for i in range(m, n + 1):
    A.append(i ** 2)
if len(A) == 0:
    print(-1)
else:
    print(sum(A))
    print(A[0])