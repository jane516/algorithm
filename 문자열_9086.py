import sys
T = int(input())
for _ in range(T):
    input = sys.stdin.readline().strip()
    start = input[0]
    end = input[-1]
    print(start, end='')
    print(end)