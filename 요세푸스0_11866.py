from collections import deque
def 요세푸스(N, K):
    my_list = deque([])
    result = []
    for i in range(N):
        my_list.append(i+1)
    while len(my_list) > 0:
        for j in range(K-1):
            a = my_list.popleft()
            my_list.append(a)
        b = my_list.popleft()
        result.append(b)
    return result


N, K = map(int, input().split())
print('<', end='')
for i in 요세푸스(N, K):
    print(i, end='')
    if i != 요세푸스(N, K)[-1]:
        print(',', end=' ')
print('>')