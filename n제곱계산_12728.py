def matrix_multi(arr1, arr2):
    result = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                result[i][j] += arr1[i][k] * arr2[k][j]
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


n = int(input())
arr = [[3, 5], [1, 3]]
my_arr = power(arr, n-1)
A = (my_arr[0][0] * 3 + my_arr[0][1])
B = int(((my_arr[1][0] * 3 + my_arr[1][1])**2 * 5)**0.5)
print(A + B)
