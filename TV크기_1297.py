import sys
case = sys.stdin.readline().strip().split()
D, H, W = int(case[0]), int(case[1]), int(case[2])
k = int((D**2 / (H**2 + W**2))**0.5)
print(H * k, W * k)