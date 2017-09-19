#Binary Converter
import program_exit
n= 0
while n < 10:
    byte = input("Byte: ")
    byte = byte.lower()
    while len(byte) == 8:
        decimal = 0
        for num in byte:
            decimal = decimal*2 + int(num)
        print(decimal)
        break
    if byte.lower() in ('exit'):
        print("Exiting software...")
        program_exit(2)
    elif len(byte) > 8 or len(byte) < 8:
        print("Not an 8 bit byte, please try again")
