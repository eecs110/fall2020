# Modify your code from Activity 8 such that the banner character
# can be any character, but defaults to the asterik character if
# no banner characted argument is specified

# Additional practice:
# Consider the following code:

def print_message(name: str, banner_character: str='*'):
    num_stars = len(name) + 7
    print(banner_character * num_stars)
    print('Hello', name, end='!\n')
    print(banner_character * num_stars)
    print('')

print_message('Varun', banner_character='~')
print_message('Jackie')
print_message('Jessica', banner_character='#')
print_message('Ana', banner_character='$')
# Write a function that prints a message for any name 
# with enough stars to exactly match the length of the message.