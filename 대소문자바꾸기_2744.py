from collections import deque
my_list = list(input())
queue = deque(my_list)
result = []
while queue:
    a = queue.popleft()
    if a.isupper():
        b = a.lower()
        result.append(b)
    else:
        b = a.upper()
        result.append(b)
for i in result:
    print(i, end='')