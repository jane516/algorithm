import sys

N, M = map(int, sys.stdin.readline().strip().split())

A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))

C = A + B


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list

    mid = len(my_list) // 2
    list1 = merge_sort(my_list[:mid])
    list2 = merge_sort(my_list[mid:])

    i, j = 0, 0
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


print(*merge_sort(C))