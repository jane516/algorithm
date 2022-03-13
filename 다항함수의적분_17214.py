f = input()
if 'x' in f:
    X = f.index('x')
    if f[-1] == 'x':
        a, b = int(f[:X]) // 2, 0
    else:
        a, b = int(f[:X]) // 2, f[X+1:]
    if b == 0:
        if a == 1:
            print('xx+W')
        elif a == -1:
            print('-xx+W')
        else:
            print(f'{a}xx+W')
    else:
        if a == 1:
            if int(b[1:]) == 1:
                print(f'xx{b[0]}x+W')
            else:
                print(f'xx{b}x+W')
        elif a == -1:
            if int(b[1:]) == 1:
                print(f'-xx{b[0]}x+W')
            else:
                print(f'-xx{b}x+W')
        else:
            if int(b[1:]) == 1:
                print(f'{a}xx{b[0]}x+W')
            else:
                print(f'{a}xx{b}x+W')
else:
    if int(f):
        if f == '1':
            print('x+W')
        elif f == '-1':
            print('-x+W')
        else:
            print(f'{f}x+W')
    else:
        print('W')