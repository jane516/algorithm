num_list = []
for _ in range(28):
    num_list.append(int(input()))
num_list.sort()
Sum = sum(num_list)
Sum2 = 30 * 31 // 2
k = 0
for i in range(1, 30):
    if num_list[i-1] != i:
        k = i
        print(i)
        break
print(Sum2 - Sum - k)