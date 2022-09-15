import sys

W, H, X, Y, P = map(int, sys.stdin.readline().strip().split())
cnt = 0


def is_in(x, y):
    check = 0
    if X <= x <= X + W:
        if Y <= y <= Y + H:
            check = 1
            return check
    else:
        dist1 = (x - X) ** 2 + (y - Y - H // 2) ** 2
        dist2 = (x - X - W) ** 2 + (y - Y - H // 2) ** 2
        if dist1 <= (H // 2) ** 2 or dist2 <= (H // 2) ** 2:
            check = 1
            return check
    return check


for _ in range(P):
    x, y = map(int, sys.stdin.readline().strip().split())
    if is_in(x, y):
        cnt += 1
print(cnt)
