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
        if byte == 'Exit':
            print("Exiting software")
            break
    else:
        print("Whoops that is not an 8 bit byte. Try again,")
    




