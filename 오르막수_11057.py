N = int(input())


def Combination(n, r):
    분자 = 분모 = 1
    for i in range(r):
        분자 *= n-i
        분모 *= (i+1)
    return 분자 // 분모 % 10007


if N < 9:
    print(Combination(9+N, N))
else:
    print(Combination(9+N, 9))