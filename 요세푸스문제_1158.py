from collections import deque
N, K = map(int, input().split())
result_list = []
num_list = deque([i+1 for i in range(N)])
count = 1
while num_list:
    X = num_list.popleft()
    if count == K:
        result_list.append(X)
        count = 1
    else:
        num_list.append(X)
        count += 1
print('<', end='')
for i in range(N):
    if i == N - 1:
        print(result_list[i], end='')
    else:
        print(result_list[i], end=', ')
print('>')