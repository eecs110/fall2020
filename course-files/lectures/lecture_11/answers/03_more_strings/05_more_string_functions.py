# This loop keeps going until the user has entered a valid age:
while True:
    age = input('enter your age: ')
    year = input('enter a year in the future: ')
    try:
        print('Your age in 2050:', int(age) + int(year) - 2019)
    except:
        # Note: this code uses the string "format" method.
        print('Both your age and year should be an integer')
    
    what_now = input('Do you want to try again (Y/n)?' )
    if what_now.upper() == 'N':
        # Exit the loop...
        print('exiting...\n')
        break
    