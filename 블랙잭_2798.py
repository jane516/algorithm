import sys
N, M = map(int, input().split())
case = sys.stdin.readline().strip()
a = list(map(int, case.split()))
b = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            result = a[i] + a[j] + a[k]
            T = M - result
            if T >= 0:
                b.append(T)
b.sort()
print(M - b[0])