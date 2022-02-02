n, m = map(int, input().split())


def 오의개수(N):
    A = 5
    Sum = 0
    while N // A > 0:
        Sum += N // A
        A *= 5
    return Sum


def 이의개수(N):
    A = 2
    Sum = 0
    while N // A > 0:
        Sum += N // A
        A *= 2
    return Sum


result1 = 오의개수(n) - 오의개수(m) - 오의개수(n-m)
result2 = 이의개수(n) - 이의개수(m) - 이의개수(n-m)
print(min(result1, result2))