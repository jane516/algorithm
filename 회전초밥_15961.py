import sys

N, d, k, c = map(int, sys.stdin.readline().strip().split())
belt = []
for i in range(N):
    chobob = int(sys.stdin.readline().strip())
    belt.append(chobob)
belt = belt + belt[:k - 1]

Max = 0
for start in range(N):
    result = [c]
    end = start + k
    result += belt[start:end]
    Max = max(Max, len(set(result)))

print(Max)