import sys
N = sys.stdin.readline().strip()
r = int(N[-1]) % 5
if r == 2 or r == 0:
    print('CY')
else:
    print('SK')