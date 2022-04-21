T = int(input())
for i in range(T):
    N = input()
    d = len(N)
    N2 = int(N) ** 2
    if str(N2)[-len(N):] == N:
        print('YES')
    else:
        print('NO')
