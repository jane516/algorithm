S = list(input())
T = list(input())


def AB1(S, T):
    if len(S) == len(T):
        if T == S:
            print(1)
            exit(0)
        return

    str1 = T
    str1.pop()
    T1 = str1
    str2 = T
    str2.reverse()
    str2.pop()
    T2 = str2
    return AB1(S, T1), AB1(S, T2)


AB1(S, T)
print(0)



