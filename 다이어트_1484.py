G = int(input())
my_list = []
for i in range(1, int(G ** 0.5) + 1):
    if G % i == 0:
        my_list.append(i)
my_list.reverse()
현재_list = []
for j in my_list:
    if (j + G // j) % 2 == 0 and j != G // j:
        print((j + G // j) // 2)
        현재_list.append((j + G // j) // 2)
if len(현재_list) == 0:
    print(-1)