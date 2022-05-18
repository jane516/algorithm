import sys


def matrix_multi(arr1, arr2):
    result = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                result[i][j] += (arr1[i][k] * arr2[k][j]) % 10000
    return result


def power(Matrix, n):
    if n == 1:
        return Matrix
    else:
        if n % 2 == 0:
            temp = power(Matrix, n // 2)
            return matrix_multi(temp, temp)
        else:
            temp = power(Matrix, n-1)
            return matrix_multi(temp, Matrix)


while True:
    n = int(sys.stdin.readline().strip())
    if n == -1:
        break
    arr = [[1, 1], [1, 0]]
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        arr = power(arr, n-1)
        print(arr[0][0] % 10000)