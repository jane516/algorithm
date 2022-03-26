import sys
case = sys.stdin.readline().strip().split()
D, H, W = int(case[0]), int(case[1]), int(case[2])
RH2, RW2 = H**2 * (D**2 / (H**2 + W**2)), W**2 * (D**2 / (H**2 + W**2))
print(int(RH2**0.5), int(RW2**0.5))