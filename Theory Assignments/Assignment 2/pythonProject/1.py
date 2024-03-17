def exponent(m,n):
    if n == 0:
        return 1
    x = exponent(m, n // 2)
    if n % 2 == 0:
        return x * x
    else:
        return x * x * m

print(exponent(3,2))