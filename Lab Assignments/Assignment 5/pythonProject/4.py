def DecimalToBinary(num):
        if num >= 1:
            if num//2 != 0:
                DecimalToBinary(num // 2)
            print(num % 2, end='')
        else:
            print(0)


DecimalToBinary(5)
print()
DecimalToBinary(10)
print()
DecimalToBinary(100)
print()
DecimalToBinary(1)
print()
DecimalToBinary(0)