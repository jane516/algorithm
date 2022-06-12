import sys
N, M = map(int, sys.stdin.readline().strip().split())
lamp_list = []
for _ in range(N):
    status = sys.stdin.readline().strip()
    lamp_list.append(status)
K = int(sys.stdin.readline().strip())
M = 0
for i in range(N):
    cnt = 0
    for num in lamp_list[i]:
        if num == '0':
            cnt += 1
    result = 0
    if cnt <= K and cnt % 2 == K % 2:
        for j in range(N):
            if lamp_list[i] == lamp_list[j]:
                result += 1
    M = max(M, result)
print(M)
