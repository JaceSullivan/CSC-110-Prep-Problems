###Jason Sullivan
###CSC 110
###This program will use functions to calculate the average between varying amounts of user input.

def average_numbers(n):
    total = 0
    average = 0
    iterations = n
    while iterations > 0:
        user_number = int(input('Number:\n'))
        total = total + user_number
        iterations = iterations - 1
#finding average
        average = round(((total/n)),2)
    print('Average =', average)


