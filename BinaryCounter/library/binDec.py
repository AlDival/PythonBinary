#Binary to decimal converter
def user_menu():
  user_input = input('''Welcome to "binary to decimal" converter
  [1]-Run the program
  [2]-Exit
  [3]-View authors\n''')
  
  if user_input == '1':
    binary = input("Enter A byte\n")
    print(binDec(binary))
  elif user_input == '2':
    exit(2)
  elif user_input == '3':
    print("Made by: DogeSec and Darth22345.")
    user_menu()

def binDec(byte):
    while len(byte) == 8:
        decimal = 0
        for num in byte:
            if num == '1' or num == '0': #only computes data in base 2
                decimal = decimal*2 + int(num)
        return (decimal)
    if len(byte) > 8 or len(byte) < 8: #Check length of the binary number
        print("Not an 8 bit byte, please try again.")

if __name__ == '__main__':
    user_menu()
  
