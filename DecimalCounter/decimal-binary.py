import math 
def base2(num):
    return num**int(math.log(num, 2)) #generates the closest lower base2 number to the number provided

number = int(input("Number: "))

print(base2(number))
