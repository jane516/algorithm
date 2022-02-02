def matrix_multi(arr1, arr2):
    result = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                result[i][j] += (arr1[i][k] * arr2[k][j]) % 1000000007
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


n = int(input())
arr = [[1, 1], [1, 0]]
if n == 1:
    print(1)
else:
    arr1 = power(arr, n)
    arr2 = power(arr, n-1)
    print(arr1[0][0] * arr2[0][0] % 1000000007)