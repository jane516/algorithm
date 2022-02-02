import sys
N = int(input())
A = [0] * N
case = sys.stdin.readline().strip().split()
for i in range(N):
    A[i] = int(case[i])
if N == 1:
    print('A')
elif N == 2:
    if A[0] != A[1]:
        print('A')
    else:
        print(A[0])
else:
    Check = 1
    if A[0] == A[1]:
        for i in range(N):
            if A[0] != A[i]:
                print('B')
                Check = 0
                break
        if Check == 1:
            print(A[0])
    else:
        K1 = A[1] - A[0]
        K2 = A[2] - A[1]
        a = K2 // K1
        b = K1 - A[0] * (a - 1)
        for i in range(1, N):
            if A[i] != A[i-1] * a + b:
                print('B')
                Check = 0
                break
        if Check == 1:
            print(A[-1] * a + b)
