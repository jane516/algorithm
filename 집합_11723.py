import sys
M = int(sys.stdin.readline().strip())
S = set()
for i in range(M):
    case = sys.stdin.readline().strip().split()
    if len(case) == 1:
        if case[0] == 'all':
            S = set([j for j in range(1, 21)])
        else:
            S = set()
    else:
        name, x = case[0], int(case[1])
        if name == 'add':
            S.add(x)
        elif name == 'remove':
            S.discard(x)
        elif name == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif name == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)

