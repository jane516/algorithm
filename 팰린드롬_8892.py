T = int(input())
for i in range(T):
    k = int(input())
    str_list = []
    check = 0
    for j in range(k):
        str_list.append(input())
    for j in range(k):
        for t in range(k):
            if j != t:
                s = str_list[j] + str_list[t]
                if s[::] == s[::-1]:
                    print(s)
                    check = 1
                    break
        if check == 1:
            break
    if check == 0:
        print(0)


