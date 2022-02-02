import sys
while True:
    case = input()
    check = 1
    if case == '.':
        break
    else:
        case = list(case)
        A = []
        count1 = count2 = count3 = count4 = 0
        for i in range(len(case)):
            if case[i] == '[':
                A.append(case[i])
                count1 += 1
            elif case[i] == ']':
                count2 += 1
                if count2 > count1:
                    check = 0
                    break
                if A[-1] == '[':
                    A.pop()
            elif case[i] == '(':
                count3 += 1
                A.append(case[i])
            elif case[i] == ')':
                count4 += 1
                if count4 > count3:
                    check = 0
                    break
                if A[-1] == '(':
                    A.pop()
        if len(A) == 0 and check == 1:
            print('yes')
        else:
            print('no')
