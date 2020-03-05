# Author : 
# Input : decimal number decNum
# Outputs : binary number
# Contributors: LucidProgramming on youtube

def dec2Bin(decNum):
  stack = []

  while decNum > 0:
    rem = decNum % 2
    stack.append(rem)
    decNum = decNum // 2

  binNum = ""
  while not len(stack) == 0:
    binNum += str(stack.pop())

  return binNum

theNumber = int(input("Enter number to convert: "))

print(dec2Bin(theNumber))