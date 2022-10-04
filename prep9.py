###Jason Sullivan
###CSC 110
###Prep 9 - Program will accept an inpput of a positive integer.  The program will then calculate the factorial value for that number.
number = int(input('Enter factorial to calculate:\n'))
print(' ')
factorial = 1
i = 1
while i <=number:
    factorial *= i
    i += 1
print(str(number) + ' factorial = '+ str(factorial))
