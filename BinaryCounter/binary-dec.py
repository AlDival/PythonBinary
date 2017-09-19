#Binary Converter
n= 0
while n < 10:
    byte = input("Byte: ")
    while len(byte) == 8:
        decimal = 0
        for num in byte:
            decimal = decimal*2 + int(num)
        print(decimal)
        break
    if byte == 'Exit' or byte == 'exit':
        print("Exiting software")
        break
    elif len(byte) > 8 or len(byte) < 8:
        print("Not an 8 bit byte, please try again")




