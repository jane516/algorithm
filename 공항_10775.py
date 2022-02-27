import sys
G = int(sys.stdin.readline().strip())
P = int(sys.stdin.readline().strip())
visited = [0 for _ in range(G + 1)]
count = 0
gate_list = []
for i in range(P):
    g = int(sys.stdin.readline().strip())
    gate_list.append(g)
for i in gate_list:
    check = 0
    for j in range(i, 0, -1):
        if not visited[j]:
            visited[j] = 1
            check = 1
            count += 1
            break
    if check == 0:
        break
print(count)
