# Write a function that prints a message for any name 
# with enough stars to exactly match the length of the message.
# Hint: Use the len() function.

def print_message(first_name:str, symbol:str='*'):
    message = 'Hello ' + first_name + '!'
    print(symbol * len(message))
    print(message)
    print(symbol * len(message))
    print()

def print_message_alt(first_name:str):
    symbol = input('Enter your favorite symbol (one character only please): ')
    if symbol == '':
        symbol = '*'
    message = 'Hello ' + first_name + '!'
    print(symbol * len(message))
    print(message)
    print(symbol * len(message))
    print()




# invoking it...
# my_symbol = input('Enter your favorite symbol (one character only please): ')
print_message('Sarah', symbol='%')
print_message('Caroline', symbol='$')
print_message('Peter', '^')
print_message('Matthew')
