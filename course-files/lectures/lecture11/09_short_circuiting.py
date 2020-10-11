def func_1():
    print('func_1 executing...')
    return False

def func_2():
    print('func_2 executing...')
    return True

# note that both functions called b/c a 
# True return value for func_2 will make the 
# whole statement True.
print('\nboth functions execute...')
if func_1() or func_2():
    print('One of the expressions is True!')



# note that func_2 never gets called because
# the program knows that if func_1 is False, 
# then the and operator will make the whole 
# statement False.
print('\nShort circuiting...')
if func_1() and func_2():
    print('Both of the expressions are True!')
else:
    print('At least one of the expressions is False')
