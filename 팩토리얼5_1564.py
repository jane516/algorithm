def Factorial5(N):
    result = 1
    for i in range(N):
        result *= (i+1)
        while result % 10 == 0:
            result //= 10
        result %= 10 ** 12
    return result % 10 ** 5


N = int(input())
n = Factorial5(N)
A = []
for i in range(5):
    A.append(n % 10)
    n //= 10
for i in range(4, -1, -1):
    print(A[i], end='')