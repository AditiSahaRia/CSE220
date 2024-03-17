def recurv(n, h, space):
    if n == 1:
        print('  '*(h-space), end='')
        print(n, end=' ')
    else:
        recurv(n-1, h, space)
        print(n, end=' ')

def line(s, h):
    if s == 1:
        return
    else:
        line(s-1, h)
        if s!=2:
            print()
        recurv(s-1, h, s-1)

val = 5
s = line(val+1, val)
