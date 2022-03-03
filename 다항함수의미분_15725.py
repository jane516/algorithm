f = input()
if 'x' in f:
    f.split('x')
    d = f.index('x')
    if f[0] == 'x':
        print(1)
    elif f[0:d] == '-':
        print(-1)
    else:
        d = f.index('x')
        print(f[0:d])
else:
    print(0)