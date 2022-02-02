S, K = map(int, input().split())
a = S // K
b = S % K
result = a ** (K - b) * (a + 1) ** b
print(result)
