import sys

S = sys.stdin.readline().strip()
P = sys.stdin.readline().strip()

if len(S) < len(P):
    print(0)
    sys.exit(0)

two_list = [1 for _ in range(len(P))]
for i in range(len(P) - 1):
    two_list[i+1] = two_list[i] * 2 % 1000000007

check = 0

SumP, SumS = 0, 0
for i in range(len(P)):
    SumP += ord(P[i]) * two_list[-1 - i] % 1000000007
    SumS += ord(S[i]) * two_list[-1 - i] % 1000000007

SumP %= 1000000007
SumS %= 1000000007

if SumP == SumS:
    print(1)
    sys.exit(0)

for i in range(len(S) - len(P)):
    SumS -= ord(S[i]) * two_list[-1]
    SumS *= 2
    SumS += ord(S[len(P)+i])
    SumS %= 1000000007
    if SumS == SumP:
        check = 1
        print(1)
        break
if check == 0:
    print(0)