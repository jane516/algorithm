S = input()
T = input()


def AB(str1, str2):
    if str1 == str2:
        return 1
    else:
        if list(str2).pop()