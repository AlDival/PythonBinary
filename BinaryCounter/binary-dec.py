#Binary Converter
n= 0
while n < 10:
    byte = input("Byte: ")
    decimal = 0
    for num in byte:
        decimal = decimal*2 + int(num)
    print(decimal)
    




