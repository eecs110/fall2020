# Additional practice:
# Consider the following code:

def print_message(name: str):
    num_stars = len(name) + 7
    print('*' * num_stars)
    print('Hello', name, end='!\n')
    print('*' * num_stars)
    print('')

print_message('Varun')
print_message('Jackie')
print_message('Jessica')
print_message('Ana')
# Write a function that prints a message for any name 
# with enough stars to exactly match the length of the message.