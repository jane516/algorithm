N = int(input())
a = list(map(int, input().split()))
Sum1 = Sum2 = 0
for i in range(N):
    Sum1 += a[i]
for j in a:
    Sum2 += j * (Sum1 - j)
print(Sum2 // 2)