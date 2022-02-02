N = int(input())
A = []
Check = 0
for i in range(N):
    A.append(int(input()))
A.sort()
A.reverse()
for i in range(N-2):
    if A[i] < A[i+1] + A[i+2]:
        Check = 1
        print(A[i]+A[i+1]+A[i+2])
        break
if Check == 0:
    print(-1)