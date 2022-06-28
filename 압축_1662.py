import sys

S = sys.stdin.readline().strip()
stack = []
length = 0
k = ''
for i in S:
    if i.isdigit():
        length += 1
        k = i
    elif i == '(':
        stack.append((k, length - 1))
        length = 0
    else:
        a, b = stack.pop()
        length = (int(a) * length) + b
print(length)