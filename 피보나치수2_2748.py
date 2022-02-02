dic = {1:0, 1:1}


def Fibonacci(n):
    if n in dic:
        return dic[n]
    else:
        result = Fibonacci(n-1) + Fibonacci(n-2)
        dic[n] = result
        return result


n = int(input())
print(Fibonacci(n))