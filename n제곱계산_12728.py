def matrix_multi(arr1, arr2):
    result = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                result[i][j] += arr1[i][k] * arr2[k][j] % 10000
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


T = int(input())
for i in range(T):
    n = int(input())
    arr = [[6, -4], [1, 0]]
    my_arr = power(arr, n - 1)
    A = my_arr[0][0] * 6 + my_arr[0][1] * 2
    print('Case #{}: {:03}'.format(i + 1, (A - 1) % 1000))
