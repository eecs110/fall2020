if True:
    print('True always evaluates to True')
    
if 1:
    print('1 also evaluates to True')

if 'Walter':
    print('any non-null or non-False value also evaluates to True')

if False:
    # will not execute
    print('False always evaluates to False')
    
if 0:
    # will not execute
    print('0 always evaluates to False')
  
if None:
    # will not execute
    print('None always evaluates to False')

if not False:
    print('not False always evaluates to True')
    
if not 0:
    print('not 0 always evaluates to True')
  
if not None:
    print('not None always evaluates to True')


# expressions and other operators can also be part of a conditional:
def check_password(password:str, username:str):
    # some logic...
    return True

if check_password('12345678', 'tylan98'):
    print('Login...')
else:
    print('Try again...')


# simplifying
my_list = [1, 2, 3]
# instead of...

if len(my_list) != 0:
   print('Not empty!')

if my_list:
   print("Not empty!")