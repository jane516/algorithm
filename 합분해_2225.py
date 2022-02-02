dic = {0:1, 1:1}


def Factorial(n):
    if n in dic:
        return dic[n]
    else:
        result = Factorial(n-1) * n
        dic[n] = result
        return result


N, K = map(int, input().split())
result = (Factorial(N)//(Factorial(K) * Factorial(N-K))) % 10007
print(int(result))