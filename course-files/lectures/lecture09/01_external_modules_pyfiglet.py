'''
NOTE: This code requires a third party module called pyfiglet. 
You will need to install this module from the command line before
this code can run. To do it, open up the Terminal (Mac) or Command 
Prompt (Windows) and type the following command (from any directory):

$ pip3 install pyfiglet

'''

# imports a module
import pyfiglet

# help(pyfiglet)
# help(pyfiglet.figlet_format)
# print('Available fonts:', pyfiglet.Figlet().getFonts())
# print('Available fonts:', *pyfiglet.Figlet().getFonts(), sep='\n')


def print_fancy_greeting(name, font='contessa'):
    # available fonts: http://www.figlet.org/examples.html
    # here are some other font options:
    # starwars, contessa, cosmic, cyberlarge
    greeting = 'Hello, ' + name + '!'
    ascii_representation = pyfiglet.figlet_format(greeting, font=font)
    print(ascii_representation)


# ask someone for their first and last name:
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

# print a greeting:
print_fancy_greeting(first_name + ' ' + last_name)
print_fancy_greeting(first_name + ' ' + last_name, font='starwars')
print_fancy_greeting(first_name + ' ' + last_name, font='weird')
print_fancy_greeting(first_name + ' ' + last_name, font='graffiti')