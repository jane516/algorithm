N = int(input())
in_car = {}
visited = [0 for _ in range(N)]
count = 0
for i in range(N):
    in_car[input()] = i
for i in range(N):
    X = input()
    visited[in_car[X]] = 1
    if in_car[X] > i:
        count += 1
    elif in_car[X] <= i and sum(visited[:in_car[X] + 1]) != in_car[X] + 1:
        count += 1
print(count)
