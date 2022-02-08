def 자리수더하기(n):
    A = list(n)
    sum = 0
    for i in range(len(A)):
        sum += int(A[i])
    return str(sum)


def 삼의배수(n, k):
    if len(n) > 1:
        n = 자리수더하기(n)
        삼의배수(n, k + 1)
    else:
        if n in ['3', '6', '9']:
            print(k)
            print('YES')
            return
        else:
            print(k)
            print('NO')
            return


X = input()
삼의배수(X, 0)