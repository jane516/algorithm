E, S, M = map(int, input().split())
i = 0
E = E % 15
S = S % 28
M = M % 19
while True:
    if E == 0 and S == 0 and M == 0:
        print(15 * 28 * 19)
        break
    x = 28 * i + S
    if x % 15 == E and x % 19 == M:
        print(x)
        break
    else:
        i += 1