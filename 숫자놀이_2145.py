def 자리수더하기(N):
    Sum = 0
    while N > 0:
        Sum += N % 10
        N //= 10
    return Sum


while True:
    N = int(input())
    if N == 0:
        break
    while True:
        X = 자리수더하기(N)
        if X < 10:
            print(X)
            break
        else:
            N = 자리수더하기(X)