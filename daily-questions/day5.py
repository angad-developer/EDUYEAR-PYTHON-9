# Day 5:
# Assignment for For Loops
# 1. From range n to m, print all the numbers divisible by 5 and 7 both
# 2. Find the sum of the series 2 +22 + 222 + 2222 + .. n terms
# 	Given:
# 	number_of_terms = 5
# 	So series will become 2 + 22 + 222 + 2222 + 22222
# 	Expected output:
# 	24690
# 	Hint: 'a'*2 = 'aa'
# Assignment for While Loops
# 3. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ).
# Print the sum of all numbers. (Use while loop)
# 4.  Write a loop to find the factorial of any number
# The factorial (symbol: !) means to multiply all whole numbers from our chosen number down to 1.
# For example: calculate the factorial of 5
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Expected output:
# 120
# 5. input: python language is best programming language
# output: P-y-T-h-O-n l-A-n-G-u-A-g-E I-s b-E-s-T P-r-O-g-R-a-M-m-I-n-G L-a-N-g-U-a-G-e

#1
# rangeStart = int(input('Enter range start index : '))
# rangeEnd = int(input('Enter range end index : '))
# for element in range(rangeStart,rangeEnd):
#   if(element % 5 == 0 and element % 7 == 0):
#     print(element)

#2
# import random

# randomNumber = random.randint(1,9)
# termsCount = int(input('Please enter number of terms required : '))
# totalSum = 0
# eachTermTotal = 1
# print(f'Random number is : {randomNumber}')

# for element in range(termsCount):
#   eachTermTotal = 1
#   for index in range(element + 1):
#     eachTermTotal *= randomNumber 
#   totalSum += eachTermTotal
# print(f'Total sum is : {totalSum}')

#3
# allowInput = True
# totalSum = 0
# print('Enter random integer values (Press q to quit) : ')
# while(allowInput):
#   userInput = input('')
#   if(userInput == 'q'):
#     allowInput = False
#   else:
#     totalSum += int(userInput)
# print(f'Total sum is : {totalSum}')

#4
# import random

# randomNumber = random.randint(1,9)
# calcValue = randomNumber
# factorialValue = 1
# while(calcValue > 0):
#   factorialValue *= calcValue
#   calcValue -= 1
# print('Factorial value of {} is {}.'.format(randomNumber,factorialValue))

#5
# stringVar = 'python language is best programming language'
# for index in range(len(stringVar)):
#   elementVal = stringVar[index]
#   endVal = '-'
#   if elementVal == ' ':
#     endVal = '\n'
#   if index == (len(stringVar) - 1):
#     endVal = ''
#   elif stringVar[index + 1] == ' ':
#     endVal = ''
  
#   if index % 2 == 0:
#     print(elementVal.upper(),end=endVal)
#   else :
#     print(elementVal.lower(),end=endVal)
