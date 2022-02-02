K = int(input())
for i in range(K):
    a = list(map(str, input()))
    A = a.count('(')
    B = a.count(')')
    Sum_A = Sum_B = 0
    if A != B or a[-1] == '(':
        print('NO')
    else:
        while len(a) > 0:
            if Sum_A > Sum_B:
                print('NO')
                break
            if a[-1] == ')':
                Sum_B += 1
                a.pop()
            else:
                Sum_A += 1
                a.pop()
            if len(a) == 0:
                print('YES')