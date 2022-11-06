import sys

K = int(sys.stdin.readline().strip())
dic = {1: 0, 2: 0, 3: 0, 4: 0}
W, H = 0, 0
w_list = []
h_list = []
cnt = 0
for _ in range(6):
    dir, dist = map(int, sys.stdin.readline().strip().split())
    if dic[dir]:
        cnt += 1
        if dir in [1, 2]:
            W += dist
            w_list.append((cnt, dist))
        else:
            H += dist
            h_list.append((cnt, dist))
    else:
        dic[dir] += 1
        if dir in [1, 2]:
            W += dist
        else:
            H += dist
if w_list[0][0] == 1:
    w = w_list[0][1]
    h = H // 2 - h_list[0][1]
else:
    w = W // 2 - w_list[0][1]
    h = h_list[0][1]
S = (W // 2) * (H // 2) - w * h
ans = S * K
print(ans)