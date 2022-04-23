N, W, H = map(int, input().split())
d = W**2 + H**2
for i in range(N):
    k = int(input())
    if k**2 <= d:
        print('DA')
    else:
        print('NE')