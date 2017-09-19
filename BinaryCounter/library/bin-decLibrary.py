def bin(byte):
    byte = byte.lower()
    while len(byte) == 8:
        decimal = 0
        for num in byte:
            decimal = decimal*2 + int(num)
        print(decimal)
    elif len(byte) > 8 or len(byte) < 8:
        print("Not an 8 bit byte, please try again")