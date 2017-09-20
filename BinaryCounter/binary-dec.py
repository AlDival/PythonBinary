#Binary Converter
import program_exit
n= 0
while n < 10:
    byte = input("Byte: ")
    byte = byte.lower()
    while len(byte) == 8:
        decimal = 0
        for num in byte:
            if num == '1' or num == '0': #only computes data in base 2
                decimal = decimal*2 + int(num)
        print(decimal)
        break
    if byte.lower() in ('exit'):
        print("Exiting software...")
        program_exit(2) #exits programs in 2 seconds and with no errors
    elif len(byte) > 8 or len(byte) < 8 or decimal == 0:
        print("Not an 8 bit byte. Their might also be a problem like you entered 8 0's. please try again")
