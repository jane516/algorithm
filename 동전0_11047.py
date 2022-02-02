N, K = map(int, input().split())
A = []
count = 0
for i in range(N):
    A.append(int(input()))
for j in range(N-1, -1, -1):
    if K // A[j] != 0:
        count += K // A[j]
        K %= A[j]
    if K == 0:
        break
print(count)