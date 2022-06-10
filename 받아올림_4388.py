import sys
while True:
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == 0 and b == 0:
        break
    a, b = max(a, b), min(a, b)
    a_list = list(str(a))
    b_list = ['0'] * (len(str(a)) - len(str(b))) + list(str(b))
    check = 0
    cnt = 0
    for i in range(len(a_list)):
        Sum = 0
        if check == 1:
            Sum = int(a_list[-1-i]) + int(b_list[-1-i]) + 1
            if Sum >= 10:
                check = 1
                cnt += 1
            else:
                check = 0
        else:
            Sum = int(a_list[-1-i]) + int(b_list[-1-i])
            if Sum >= 10:
                check = 1
                cnt += 1
            else:
                check = 0
    print(cnt)