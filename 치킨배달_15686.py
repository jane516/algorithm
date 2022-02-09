import sys

N, M = map(int, input().split())
치킨 = []
집 = []
for i in range(N):
    case = sys.stdin.readline().strip().split()
    for j in range(N):
        locate = int(case[j])
        if locate == 2:
            치킨.append([i, j])
        elif locate == 1:
            집.append([i, j])
치킨거리 = [0 for _ in range(len(치킨))]
for i in range(len(치킨)):
    for j in range(len(집)):
        치킨거리[i] += abs(치킨[i][0] - 집[j][0]) + abs(치킨[i][1] - 집[j][1])
치킨거리2 = 치킨거리
치킨거리2.sort()
print(치킨거리)
print(치킨)
