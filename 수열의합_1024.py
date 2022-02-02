def 짝수길이(N, L):
    while True:
        if L > 100 or N < L * (L - 1) // 2:
            return 0
            break
        elif (N - L // 2) % L == 0:
            return L
            break
        L += 2


def 홀수길이(N, L):
    while True:
        if L > 100 or N < L * (L - 1) // 2:
            return 0
            break
        elif N % L == 0:
            return L
            break
        L += 2


N, L = map(int, input().split())
if L % 2 == 0:
    L_1 = 짝수길이(N, L)
    L_2 = 홀수길이(N, L + 1)
else:
    L_1 = 짝수길이(N, L + 1)
    L_2 = 홀수길이(N, L)
if min(L_1, L_2) != 0:
    if L_1 < L_2:
        for i in range(0, L_1):
            print((N - L_1 // 2) // L_1 - L_1 // 2 + 1 + i, end=' ')
    else:
        for i in range(0, L_2):
            print(N // L_2 - (L_2 - 1) // 2 + i, end=' ')
elif min(L_1, L_2) == 0 and max(L_1, L_2) != 0:
    if max(L_1, L_2) % 2 == 0:
        for i in range(0, L_1):
            print((N - L_1 // 2) // L_1 - L_1 // 2 + 1 + i, end=' ')
    else:
        for i in range(0, L_2):
            print(N // L_2 - (L_2 - 1) // 2 + i, end=' ')
else:
    print(-1)