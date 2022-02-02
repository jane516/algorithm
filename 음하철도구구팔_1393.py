x_s, y_s = map(int, input().split())
x_e, y_e, dx, dy = map(int, input().split())
if dx == 0:
    if dy != 0:
        if y_s < y_e:
            print(x_e, y_e)
        else:
            print(x_e, y_s)
    else:
        print(x_e, y_e)
else:
    if dy == 0:
        if x_s < x_e:
            print(x_e, y_e)
        else:
            print(x_s, y_e)
    else:
        if dx * (y_e - y_s) == dy * (x_e - x_s):
            if x_s < x_e:
                print(x_e, y_e)
            else:
                print(x_s, y_s)
        else:
            x = (dx**2 * x_s + dy**2 * x_e + dy*dx*(y_s - y_e))//(dx**2+dy**2)
            y = dy * (x-x_e)//dx + y_e
            if x < x_e:
                print(x_e, y_e)
            else:
                print(x, y)