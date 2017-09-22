import math 
def base2(num):
    num = int(num)
    if num > 255:
        return("Can't fit in a byte.")
    elif num < 0:
        return("Negative numbers can't be computed at this time")
    else:
        return 2**int((math.log2(num))) #generates the closest lower base2 number to the number provided


