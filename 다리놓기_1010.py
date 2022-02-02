dic = {0:1, 1:1}


def Factorial(n):
    if n in dic:
        return dic[n]
    else:
        result = Factorial(n-1) * n
        dic[n] = result
        return result


T = int(input())
for i in range(0, T):
    N, M = map(int, input().split())
    경우의_수 = Factorial(M)/(Factorial(N)*Factorial(M-N))
    print(int(경우의_수))