S = list(input())
T = list(input())
check = 0
while True:
    if T == S:
        check = 1
        break
    if len(T) == 0:
        break
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()
if check == 1:
    print(1)
else:
    print(0)