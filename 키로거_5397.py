import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    S = sys.stdin.readline().strip()

    order = ['<', '>', '-']
    result = []
    my_list = []

    for i in S:
        if i not in order:
            result.append(i)
        else:
            if i == '<':
                if result:
                    X = result.pop()
                    my_list.append(X)
                else:
                    continue
            elif i == '>':
                if my_list:
                    X = my_list.pop()
                    result.append(X)
                else:
                    continue
            else:
                if result:
                    result.pop()
                else:
                    continue
    for i in range(len(my_list)):
        result.append(my_list[len(my_list) - 1 - i])
    for i in result:
        print(i, end='')
    print()
