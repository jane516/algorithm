import sys
N = int(sys.stdin.readline().strip())
my_list = [int(sys.stdin.readline().strip()) for _ in range(N)]
stack = []
cnt = 0
for height in my_list:
    while stack and stack[-1][0] < height:
        cnt += stack.pop()[1]
    if not stack:
        stack.append((height, 1))
        continue

    if stack[-1][0] == height:
        k = stack.pop()[1]
        cnt += k
        if stack:
            cnt += 1
        stack.append((height, k + 1))

    else:
        stack.append((height, 1))
        cnt += 1

print(cnt)