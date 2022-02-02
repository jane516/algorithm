t = int(input())
for i in range(t):
    n = int(input())
    phone_list = []
    for j in range(n):
        number = input()
        phone_list.append((len(number), number))
    phone_list.sort()
    check = 0
    for j in range(n-1):
        for k in range(j+1, n):
            if phone_list[j][1] == phone_list[k][1][:len(phone_list[j][1])]:
                check = 1
                break
    if check == 0:
        print('YES')
    else:
        print('NO')