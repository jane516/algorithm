S = input()
T = input()


def AB(s, t):
    if s == t:
        print(1)
        exit()
    if list(t)[-1] == 'A' and len(t) > len(s):
        t1 = list(t)
        t1.pop()
        AB(s, str(''.join(t1)))

    if list(t)[0] == 'B' and len(t) > len(s):
        t2 = list(t)
        t2.reverse()
        t2.pop()
        AB(s, str(''.join(t2)))


AB(S, T)
print(0)










