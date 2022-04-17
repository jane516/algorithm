import sys
case = sys.stdin.readline().strip().split()
N, M = int(case[0]), int(case[1])
tree = list(map(int, sys.stdin.readline().strip().split()))
l, r = 0, max(tree)
check = 0
Max = 0
while True:
    m = (l + r) // 2
    Sum = 0
    for i in range(len(tree)):
        if tree[i] > m:
            Sum += tree[i] - m
    if Sum == M:
        print(m)
        break
    elif Sum > M and check == 1:
        Max = m
        if l == Max:
            print(l)
            break
    if Sum > M:
        check = 1
        l = m
    else:
        r = m
