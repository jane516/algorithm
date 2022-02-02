N, M = map(int, input().split())
치킨 = []
집 = []
for i in range(N):
    for j in range(N):
        locate = int(input())
        if locate == 2:
            치킨.append([i, j])
        elif locate == 1:
            집.append([i, j])
for k in 집:
    for