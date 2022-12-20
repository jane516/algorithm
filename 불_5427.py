import sys
from collections import deque

T = int(input())
for _ in range(T):
    C, R = map(int, sys.stdin.readline().strip().split())
    miro = [[2000 for _ in range(C)] for _ in range(R)]
    Fire = deque([])
    jihun_x, jihun_y = 0, 0

    for i in range(R):
        List = sys.stdin.readline().strip()
        for j in range(C):
            if List[j] == '*':
                Fire.append((i, j))
                miro[i][j] = 1
            if List[j] == '@':
                jihun_x, jihun_y = i, j
            if List[j] == '#':
                miro[i][j] = -1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while Fire:
        fire = Fire.popleft()
        x, y = fire[0], fire[1]
        for i in range(4):
            Dx = x + dx[i]
            Dy = y + dy[i]
            if Dx < 0 or Dy < 0 or Dx >= R or Dy >= C:
                continue
            if miro[Dx][Dy] != 2000:
                continue
            miro[Dx][Dy] = miro[x][y] + 1
            Fire.append((Dx, Dy))

    queue = deque([(jihun_x, jihun_y)])
    miro[jihun_x][jihun_y] = 1
    Find = 0

    while queue:
        jihun_x, jihun_y = queue.popleft()
        if jihun_x == 0 or jihun_y == 0 or jihun_x == R - 1 or jihun_y == C - 1:
            Find = miro[jihun_x][jihun_y]
            break
        for i in range(4):
            Dx = jihun_x + dx[i]
            Dy = jihun_y + dy[i]
            if Dx < 0 or Dy < 0 or Dx >= R or Dy >= C:
                continue
            if miro[Dx][Dy] <= miro[jihun_x][jihun_y] + 1:
                continue
            miro[Dx][Dy] = miro[jihun_x][jihun_y] + 1
            queue.append((Dx, Dy))

    if Find == 0:
        print('IMPOSSIBLE')
    else:
        print(Find)