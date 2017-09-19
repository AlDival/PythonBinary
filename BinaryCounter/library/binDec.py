def binDec(byte):
    for num in byte:
        if byte[num] in ['2','3','4','5','6','7','8','9']:
            x = 1
    while len(byte) == 8 and x == 0:
        decimal = 0
        for num in byte:
            decimal = decimal*2 + int(num)
        return(decimal)
        break
    if len(byte) > 8 or len(byte) < 8:
        print("Not an 8 bit byte, please try again")
    elif x != 0:
        print("Please enter a valid binary number")

binary = input("Byte: ")
print(binDec(binary))
