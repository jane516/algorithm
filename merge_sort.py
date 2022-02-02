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


N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
a = merge_sort(a)
for j in range(N):
    print(a[j])
