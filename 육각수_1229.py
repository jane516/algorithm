import sys
N = int(sys.stdin.readline().strip())
육각수 = [2 * i**2 - i for i in range(1, 709)]
count = 0
while N > 0:
    for i in range(len(육각수)):
        if 육각수[i] > N:
            N -= 육각수[i-1]
            print(육각수[i-1])
            count += 1
            break
print(count)
print(육각수)