A, B, N = map(int, input().split())
result = (A * 10**N // B) % 10
print(result)