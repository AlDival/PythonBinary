import math 
def base2(num):
    num = int(num)
    if num > 255:
        return("Can't fit in a byte.")
    elif num < 0:
        return("Negative numbers can't be computed at this time")
    else:
        sum = num
        list = []
        for x in range(0,2**sum):
            list.append(2**int((math.log2(sum))))
            sum -= 2**int((math.log2(sum)))
            if(sum == 0):
                break
        finalString = []
        for y in range(0,8):
            if(2**y in list):
                finalString.append("1")
            else:
                finalString.append("0")
        return "".join(finalString[::-1])