# DAY 3 : ASSIGNMENT TO PUSH ON GITHUB
# AGE CALCULATOR 
# 1)  calculate Age of a person - User should enter the year of birth and the program should output the age.. eg : entered value is 1990, output age is 30
# 2) Simple Calculator:
# - get 2 numbers from the user and print the result of addition, subtraction, multiplication and floor division, decimal division, remainder, power of the input numbers

#1
import datetime

age = int(input('Please enter your year of birth : '))
presentYear = datetime.datetime.now().year
print(f'Your present age is : {presentYear - age}')

#2
num1 = int(input('Please enter first number : '))
num2 = int(input('Please enter second number : '))
print(f'Addition (A+B) of both numbers is : {num1 + num2}')
print(f'Subtraction (A-B) of both numbers is : {num1 - num2}')
print(f'Multiplication (A*B) of both numbers is : {num1 * num2}')
print(f'Floor Division (A//B) of both numbers is : {num1 // num2}')
print(f'Decimal Division (A/float(B)) of both numbers is : {num1 / float(num2)}')
print(f'Remainder (A%B) of both numbers is : {num1 % num2}')
print(f'Power (A**B) of both numbers is : {num1 ** num2}')

