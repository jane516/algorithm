import sys
n = int(sys.stdin.readline().strip())
stack = []
result = []
check = 0
k = 1
for i in range(n):
    X = int(input())
    while k <= X:
        stack.append(k)
        result.append('+')
        k += 1
    if stack[-1] == X:
        stack.pop()
        result.append('-')
    else:
        check = 1
if check == 1:
    print('NO')
else:
    for i in result:
        print(i)