###Jason Sullivan
###CSC 110
###Prep 6 - Program will print out the state of water based on the temperature fahrenheit
temp = float(input('Temperature in fahrenheit:\n'))
if temp <= 32:
    print('Ice')
elif temp >= 212:
    print('Steam')
else:
    print('Water')
