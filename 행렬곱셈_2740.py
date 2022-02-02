def matrix_multi(arr1, arr2):
    result = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                result[i][j] += (arr1[i][k] * arr2[k][j])
    return result


N, M1 = map(int, input().split())
arr1 = []
for i in range(0, N):
    list_nm = list(map(int, input().split()))
    arr1.append(list_nm)
M2, K = map(int, input().split())
arr2 = []
for j in range(0, M2):
    list_mk = list(map(int, input().split()))
    arr2.append(list_mk)
Matrix = matrix_multi(arr1, arr2)
for a in Matrix:
    for b in a:
        print(b, end=' ')
    print()