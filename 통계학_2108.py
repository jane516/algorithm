from collections import Counter


def 산술평균(N, arr):
    Sum = 0
    for i in range(N):
        Sum += arr[i]
    return round(Sum / N)


def 중앙값(N, arr):
    arr.sort()
    return arr[N // 2]


def 최빈값(arr):
    my_list = Counter(arr).most_common()
    if len(my_list) > 1 and my_list[0][1] == my_list[1][1]:
        return my_list[1][0]
    else:
        return my_list[0][0]


def 범위(arr):
    arr.sort()
    return arr[-1] - arr[0]


N = int(input())
a = []
for i in range(N):
    K = int(input())
    a.append(K)
print(산술평균(N, a))
print(중앙값(N, a))
print(최빈값(a))
print(범위(a))