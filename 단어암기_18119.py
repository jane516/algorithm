import sys
case = sys.stdin.readline().strip().split()
N, M = int(case[0]), int(case[1])
my_list = []
for i in range(N):
    word = sys.stdin.readline().strip()
    bitmask = 0
    for c in word:
        idx = ord(c) - ord('a')
        bitmask |= (1 << idx)
    my_list.append(bitmask)
check = 2**26 - 1
for i in range(M):
    case2 = sys.stdin.readline().strip().split()
    o, x = case2[0], case2[1]
    idx = ord(x) - ord('a')
    if o == '1':
        check &= ~(1 << idx)
    else:
        check |= (1 << idx)
    count = 0
    for j in my_list:
        if check & j == j:
            count += 1
    print(count)

