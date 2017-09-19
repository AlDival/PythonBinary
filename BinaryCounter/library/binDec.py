def binDec(byte):
    while len(byte) == 8:
        decimal = 0
        for num in byte:
            decimal = decimal*2 + int(num)
        return(decimal)
        break
    if len(byte) > 8 or len(byte) < 8:
        print("Not an 8 bit byte, please try again")

binary = input("Byte: ")
print(binDec(binary))