import sys
N, K = map(int, input().split())
olympic = []
count = 1
for i in range(N):
    case = sys.stdin.readline().strip().split()
    olympic.append([int(case[0]), int(case[1]), int(case[2]), int(case[3])])
olympic.sort()
for i in olympic:
    if i[1] > olympic[K - 1][1]:
        count += 1
    elif i[1] == olympic[K - 1][1]:
        if i[2] > olympic[K - 1][2]:
            count += 1
        elif i[2] == olympic[K - 1][2]:
            if i[3] > olympic[K - 1][3]:
                count += 1
print(count)
