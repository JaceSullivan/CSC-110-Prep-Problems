###Jason Sullivan
###CSC 110
###Prep 7 - Program will ask for two inputs, drink size (large and small) and drink type.  The program will then print out a description of the drink.
size = input('Drink size:\n')
type = input('Drink type:\n')
print(' ')
if type == 'regular':
    if size == 'large':
        print('300 calories')
    if size == 'small':
        print('150 calories')
if type == 'diet':
    if size == 'large':
        print('100 calories')
    if size == 'small':
        print('50 calories')
if type == 'water':
    if size == 'large':
        print('0 calories')
    if size == 'small':
        print('0 calories')