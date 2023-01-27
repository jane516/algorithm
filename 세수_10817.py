import sys

A, B, C = map(int, sys.stdin.readline().strip().split())

list = [A, B, C]
list.sort()

print(list[1])

