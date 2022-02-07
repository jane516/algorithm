S = list(input())
T = list(input())


def AB(S, T):
    str1 = T
    str2 = T
    if len(S) == len(T):
        if str1 == S or str2 == S:
            print(1)
            return
    else:
        str1.pop()
        str2.reverse()
        str2.pop()
        AB(S, str1)
        AB(S, str2)


AB(S, T)
print(0)



