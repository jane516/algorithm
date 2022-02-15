import sys


def matrix_multi(arr1, arr2):
    result = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                result[i][j] += arr1[i][k] * arr2[k][j] % 1000000000
    return result


def power(Matrix, n):
    if n == 1:
        return Matrix
    else:
        if n % 2 == 0:
            temp = power(Matrix, n // 2)
            return matrix_multi(temp, temp)
        else:
            temp = power(Matrix, n - 1)
            return matrix_multi(temp, Matrix)


case = sys.stdin.readline().strip().split()
a, b = int(case[0]), int(case[1])
arr = [[1, 1], [1, 0]]
an = 0
bn = 0
p = 0
q = 0
if a == 1:
    an = 1
else:
    an = power(arr, a - 1)[0][0]
if a - b + 1 == 1:
    p = 1
else:
    p = power(arr, b - a)[0][0]

bn = power(arr, a)[0][0]
q = power(arr, b - a + 1)[0][0]
result = p * an + (q - 1) * bn
print(result % 1000000000)