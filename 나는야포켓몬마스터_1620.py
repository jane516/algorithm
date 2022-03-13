import sys
case = sys.stdin.readline().strip().split()
N, M = int(case[0]), int(case[1])
Pokemon = {}
for i in range(N):
    name = sys.stdin.readline().strip()
    Pokemon[str(i+1)] = name
    Pokemon[name] = str(i+1)
for i in range(M):
    print(Pokemon[sys.stdin.readline().strip()])