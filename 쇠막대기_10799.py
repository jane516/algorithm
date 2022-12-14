import sys

line = sys.stdin.readline().strip()
stack = []
cnt = 0
result = 0
length = len(line)
a = line[0]

for i in range(length):
    if i != 0:
        a = line[i - 1]
    if line[i] == '(':
        stack.append(i)
    elif line[i] == ')':
        if a == '(':
            stack.pop()
            if stack:
                cnt += 1
        else:
            result += cnt + 1
            stack.pop()
print(result)
