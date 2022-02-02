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


D = int(input())
list1 = [0, 1, 1, 0, 0, 0, 0, 0]
list2 = [1, 0, 1, 1, 0, 0, 0, 0]
list3 = [1, 1, 0, 1, 1, 0, 0, 0]
list4 = [0, 1, 1, 0, 1, 1, 0, 0]
list5 = [0, 0, 1, 1, 0, 1, 1, 0]
list6 = [0, 0, 0, 1, 1, 0, 0, 1]
list7 = [0, 0, 0, 0, 1, 0, 0, 1]
list8 = [0, 0, 0, 0, 0, 1, 1, 0]
arr = [list1, list2, list3, list4, list5, list6, list7, list8]
arr = power(arr, D)
print(arr[0][0] % 1000000007)