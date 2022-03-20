import sys
my_list = list(sys.stdin.readline().strip().split())
a = my_list[:]
a.sort()
b = a[:]
b.reverse()
if my_list == a:
    print('ascending')
elif my_list == b:
    print('descending')
else:
    print('mixed')