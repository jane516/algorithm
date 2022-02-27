import re
S = input()
K = input()
S = re.sub(r'[0-9]', '', S)
if K in S:
    print(1)
else:
    print(0)