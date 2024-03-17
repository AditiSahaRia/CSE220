def recurv(n):
    if n == 1:
        print(n, end=' ')
    else:

        recurv(n-1)
        print(n, end=' ')
        #print(recurv(n-1), n)

def line(s):
    if s == 1:
        return
    else:

        line(s-1)
        if s!=2:
            print()
        recurv(s - 1)

val = 5
s = line(val+1)
