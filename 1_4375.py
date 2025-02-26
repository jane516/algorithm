def find_digit(n):
    cnt = 0
    Sum = 0
    start = 1
    while True:
        Sum += start % n
        cnt += 1
        if Sum % n == 0:
            break
        start *= 10
    return cnt


while True:
    try:
        n = int(input())
    except:
        break
    print(find_digit(n))