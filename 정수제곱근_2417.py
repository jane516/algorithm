n = int(input())
q = int(n ** 0.5)
for i in range(q, q + 3):
    if i ** 2 >= n:
        print(i)
        break