import re
import sys
S = sys.stdin.readline().strip()
K = sys.stdin.readline().strip()
S = re.sub(r'[0-9]', '', S)
if K in S:
    print(1)
else:
    print(0)