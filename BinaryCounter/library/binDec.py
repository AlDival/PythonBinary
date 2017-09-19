def binDec(byte):
    while len(byte) == 8:
        decimal = 0
        for num in byte:
            decimal = decimal*2 + int(num)
        return(decimal)
        break 
    if len(byte) > 8 or len(byte) < 8: #Check length of the binary number
        print("Not an 8 bit byte, please try again.")

binary = input("Byte: ")
print(binDec(binary)) #Takes "binary"'s input and passes it through the function and gives decimal result.
