import math
import time

#Decimal to binary converter
def decBin(num):
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


def user_menu():
  user_input = int(input('''Welcome to "binary to decimal" converter
  [1]-Exit
  [2]-View authors\n'''))
  

  if user_input == 1:
    exit(2)
  elif user_input == 2:
    print("Made by: DogeSec, Darth22345 and Samuelb2020.")
    user_menu()

#Binary to decimal converter
def binDec(byte):
    while len(byte) == 8:
        decimal = 0
        for num in byte:
            if num == '1' or num == '0': #only computes data in base 2
                decimal = decimal*2 + int(num)
        return (decimal)
    if len(byte) > 8 or len(byte) < 8: #Check length of the binary number
        return("Not an 8 bit byte, please try again.")


def program_exit(x):
  time.sleep(x)
  exit(2)