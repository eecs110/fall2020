# Example 1: 
# Consider the built-in function pow(), which has 2 required positional parameters: 
# (1) the base number, and (2) the exponent.  Order matters:
# You have to understand which number is which so that you can use
# the function correctly.

print(pow(3, 2))  
print(pow(2, 3))


# Example 2: Keyword parameters. Keyword parameters are optional and have a default value:
# * The default value of sep is a space ' '
# * The default value of end is a newline character '\n'

print() # prints an empty line:
name = 'Jackson'
print('Hello', 'there', name, '!')
print('Hello', 'there', name, end='!\n')
print('Hello', 'there', name, sep='~~~~~~', end='!\n')

