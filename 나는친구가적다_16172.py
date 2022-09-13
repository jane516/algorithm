import sys
S = sys.stdin.readline().strip()
K = sys.stdin.readline().strip()
result = ''
for s in S:
    if s.isalpha():
        result += s
if K in result:
    print(1)
else:
    print(0)