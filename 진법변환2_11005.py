import sys
case = sys.stdin.readline().strip().split()
N = int(case[0])
B = int(case[1])
stack = []
while N > 0:
    R = N % B
    if R >= 10:
        R = chr(R + 55)
    stack.append(R)
    N //= B
for i in range(len(stack)):
    print(stack.pop(), end='')