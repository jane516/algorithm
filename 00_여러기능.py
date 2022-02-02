"""
에라토스체네스의 체
"""
def prime_list(n):
    sieve = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i] == True]


"""
약수 구하기
"""
n, k = map(int, input().split())
a = n
result_list = [1, n]
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        result_list.append(i)
        if i != a // i:
            result_list.append(a // i)
result_list.sort()
if len(result_list) < k:
    print(0)
else:
    print(result_list[k - 1])


"""
소인수분해
"""
def prime_list(n):
    sieve = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i] == True]


def 소인수분해(n):
    A = []
    for i in prime_list(int(n ** 0.5)):
        if n % i == 0:
            A.append(i)
            while n % i == 0:
                n //= i
    if n > 1:
        A.append(n)
    return A


"""
피보나치수열 빠른재귀
"""
dic = {0: 0, 1: 1}


def Fibonacci(n):
    if n in dic:
        return dic[n]
    else:
        result = Fibonacci(n-1) + Fibonacci(n-2)
        dic[n] = result
        return result


"""
최대공약수
"""
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


"""
확장된유클리드
"""
def e_gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return [a, 1, 0]
    else:
        x1, x2 = 1, 0
        y1, y2 = 0, 1
        while b > 0:
            q = a // b
            r = a % b
            x = x1 - q * x2
            y = y1 - q * y2
            a, b = b, r
            x1, x2 = x2, x
            y1, y2 = y2, y
        return [a, x1, y1]


"""
행렬곱셈
"""
def matrix_multi(arr1, arr2):
    result = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                result[i][j] += (arr1[i][k] * arr2[k][j])
    return result


"""
행렬 거듭제곱
"""
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


"""
머지소트
"""
def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = len(my_list) // 2
    list1 = merge_sort(my_list[:mid])
    list2 = merge_sort(my_list[mid:])

    i, j, k = 0, 0, 0
    arr = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            arr.append(list1[i])
            i += 1
        else:
            arr.append(list2[j])
            j += 1
    arr += list1[i:]
    arr += list2[j:]
    return arr


"""
카운팅정렬
"""
def counting_sort(array, max):
    counting_array = [0] * (max + 1)
    for i in array:
        counting_array[i] += 1
    for i in range(max):
        counting_array[i + 1] += counting_array[i]
    output_array = [-1] * len(array)
    for i in array:
        output_array[counting_array[i] - 1] = i
        counting_array[i] -= 1
    return output_array


"""
외적
"""
def cross_product(x1, y1, x2, y2, x3, y3):
    answer = 0
    P = x1 * y2 + x2 * y3 + x3 * y1
    M = x2 * y1 + x3 * y2 + x1 * y3
    if P - M < 0:
        answer = -1  # 시계 방향
    elif P - M == 0:
        answer = 0
    else:
        answer = 1  # 반시계 방향
    return answer