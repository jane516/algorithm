def 정수(a, b):
    if a / b == a // b:
        return 1
    else:
        return 0


T = int(input())
for _ in range(T):
    cnt = 0
    n, m = map(int, input().split())
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if 정수(i**2 + j**2 + m, i * j) == 1:
                cnt += 1
    print(cnt)
