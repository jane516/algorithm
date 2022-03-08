import re
S = input()
S = re.sub(r'[^CPU]', '', S)
check = 0
for i in range(len(S)):
    if S[i] == 'U' and check == 0:
        check = 1
    elif S[i] == 'C' and check == 1:
        check = 2
    elif S[i] == 'P' and check == 2:
        check = 3
    elif S[i] == 'C' and check == 3:
        check = 4

if check == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')