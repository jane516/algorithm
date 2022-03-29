import sys
N = int(input())
case = sys.stdin.readline().strip().split()
Sum = 0
저울추 = [0 for _ in range(N)]
for i in range(N):
    저울추[i] = int(case[i])
저울추.sort()
for i in range(N):
    if Sum + 1 >= 저울추[i]:
        Sum += 저울추[i]
    else:
        break
print(Sum + 1)