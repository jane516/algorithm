N = int(input())
a = []
b = []
for i in range(N):
    x, y = map(int, input().split())
    a.append((x, y))
for j in range(N):
    count = 1
    for k in range(N):
        if a[j][0] < a[k][0] and a[j][1] < a[k][1]:
            count += 1
    b.append(count)
for t in range(len(a)):
    print(b[t], end=' ')