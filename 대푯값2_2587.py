a = [0 for _ in range(5)]
for i in range(5):
    a[i] = int(input())
print(sum(a) // 5)
a.sort()
print(a[2])