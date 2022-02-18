A, B = map(int, input().split())
C = int(input())
result = A * 60 + B + C
result %= 1440
H = result // 60
M = result % 60
print(H, M)