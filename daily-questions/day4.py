# Day 4:
# 1) use string functions to count the occurrence of 'y' in a word given by user.
# 2) take input of a string and print it's even indexed characters
# 3)create a program to swap case. Using string functions
# Input : EdUyEaR
# Output :.  eDuYeAr

#1
charCountString = input('Please enter some random string : ')
print(f'Number of "y" in the string are {charCountString.count("y")}')

#2
evenIndexCountString = input('Please enter some random string : ')
print(f'Number of even indexed chars in the string are {(len(evenIndexCountString) // 2)}')

#3
reverseString = input('Enter random case string : ')
print(f'Input : {reverseString}')
print(f'Output : {reverseString.swapcase()}')
