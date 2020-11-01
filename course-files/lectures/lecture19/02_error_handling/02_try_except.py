# Challenge: write some code that will handle any user input
# errors so that if the user enters a value that is invalid,
# the program tells the user what their error is and prompts
# them again:
while True:
    age = input('enter your age: ')
    year = input('enter a year in the future: ')
    print('Your age in 2050:', int(age) + int(year) - 2020)

    up_next = input('Do you want to try again (Y/n)?' )
    if up_next.upper() == 'N':
        # Exit the loop...
        print('exiting...\n')
        break