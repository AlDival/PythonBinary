import math 
def base2(num):
    return 2**round((math.log2(num))) #generates the closest lower base2 number to the number provided

number = int(input("Number: "))#Just here for testing purposes
print(base2(number))#Just here for testing purposes
