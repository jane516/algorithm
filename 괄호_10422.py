def Factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i % 1000000007
    return result


T = int(input())
for i in range(T):
    L = int(input())
    if L % 2 == 1:
        print(0)
    else:
        X = Factorial(L)
        Y = Factorial(L // 2)
        R = X * pow(Y * Y * (L // 2 + 1), 1000000005, 1000000007) % 1000000007
        print(R)