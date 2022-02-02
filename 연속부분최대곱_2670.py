N = int(input())
A = [1] * N
for i in range(N):
    A[i] = float(input())
max_list = [1] * N
max_list[0] = A[0]
for j in range(1, N):
    max_list[j] = max(A[j], max_list[j-1] * A[j])
print("%.3f" % max(max_list))