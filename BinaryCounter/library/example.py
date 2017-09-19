import binDec

try:
  binary = int(input("Byte: "))
  print(binDec(binary))
except ValueError:
  print("Please insert a binary")
  exit(2)
