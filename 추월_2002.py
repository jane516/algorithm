N = int(input())
in_car = []
out_car = []
else_car = []
for i in range(N):
    in_car.append(input())
for j in range(N):
    X = input()
    if X == in_car[j]:
        out_car.append(X)