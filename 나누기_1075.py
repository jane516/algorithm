import sys
N = int(sys.stdin.readline().strip())
F = int(input())
for i in range(100):
    X = (N // 100) * 100 + i
    if X % F == 0:
        print('%02d' % (X % 100))
        break