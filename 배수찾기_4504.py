n = int(input())
my_list = []
while True:
    a = int(input())
    if a == 0:
        break
    else:
        my_list.append(a)
for i in range(len(my_list)):
    if my_list[i] % n == 0:
        print('%d is a multiple of %d.' %(my_list[i], n))
    else:
        print('%d is NOT a multiple of %d.' %(my_list[i], n))
