import sys
N = int(sys.stdin.readline().strip())
r = N % 7
if r == 0 or r == 2:
    print('CY')
else:
    print('SK')