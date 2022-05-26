import sys
T = int(input())
for i in range(T):
    a = int(sys.stdin.readline().strip())
    l, r = 0, a
    x = -1
    while True:
        if abs(x - a**(1/3)) < 1e-18:
            break
        m = (l + r) / 2
        x = r
        if m < a ** (1 / 3):
            l = m
        else:
            r = m

    answer = str(x)
    if '.' in answer:
        k = answer.index('.')
        if len(answer[k+1:]) > 10:
            print(answer[:k+11])
        else:
            print(answer)
    else:
        print(answer)