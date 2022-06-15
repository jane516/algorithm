import sys
king, stone, N = sys.stdin.readline().strip().split()
kx, ky = int(king[0]) - 96, int(king[1])
sx, sy = int(stone[0]) - 96, int(stone[1])

for _ in range(N):
    order = sys.stdin.readline().strip()
    if len(order) == 1:
        if order == 'R':
            if kx <= 8:
                kx += 1
            else:
                continue
        elif order == 'L':
            if 1 <= kx - 1:
                kx -= 1
            else:
                continue
        elif order == 'B':
            if 1 <= ky - 1:
                ky -= 1
            else:
                continue
        else:
            if ky + 1 <= 8:
                ky += 1

