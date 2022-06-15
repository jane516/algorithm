import sys
K, L = map(int, sys.stdin.readline().strip().split())
for i in range(2, int(K ** 0.5) + 1):
    a = K % i
    if a == 0 and i >= L:
        print('GOOD')
        break
    elif a == 0 and i < L:
        print('BAD', i)
        break