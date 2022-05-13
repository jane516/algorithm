import sys
t = int(input())
for i in range(t):
    n = int(sys.stdin.readline().strip())
    phone_list = []
    for j in range(n):
        number = input()
        phone_list.append(number)
    phone_list.sort()
    check = 0
    for j in range(n-1):
        if len(phone_list[j]) < len(phone_list[j+1]):
            if phone_list[j+1][:len(phone_list[j])] == phone_list[j][:]:
                check = 1
                break
    if check == 0:
        print('YES')
    else:
        print('NO')