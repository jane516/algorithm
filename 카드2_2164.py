from collections import deque


def 카드2(arr):
    if len(arr) == 1:
        return arr
    else:
        while len(arr) > 1:
            if len(arr) == 1:
                break
            arr.popleft()
            arr.append(arr[0])
            arr.popleft()
        return arr


N = int(input())
queue = deque([])
for i in range(N):
    queue.append(i + 1)
print(카드2(queue)[0])