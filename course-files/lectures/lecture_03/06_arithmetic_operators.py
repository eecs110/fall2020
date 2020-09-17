########################
# Arithmetic Operators #
########################

# 1.1. Numbers
# initialize variables for demo:
a = 20
b = 10
c = 25
print(a + b)    # addition
print(a - b)    # subtraction
print(a * b)    # multiplication
print(b / a)    # division (notice the result is a float)
print(c % a)    # modulus  25 / 20 = 1 with 5 left over (remained = 5)
print(c // a)  # quotient  25 / 20 = 1 with 5 left over (quotient = 1)
print(a ** b)  # exponent
print(c ** (1/2))  # square root (notice the result is a float)



# 1.2. Strings
print('34' + '34')  # in the context of a string, the + sign concatenates two strings
# Note: not all operators work with all datatypes. 
# Uncomment the line below to see what happens.
# print('34' - '34')
print('34' * 100)  # but multiplication does work. In the context of a string, the * sign repeats the string n times.
# Note: again, not all operators work with all datatypes. 
# Uncomment the line below to see what happens.
# print('34' * '34')


# 1.3. Booleans
# True implicitly converted to 1, False implicitly converted to 0.
# same as: 1 + 1 + 0 + 0 + 1
print(True + True + False + False + True)
# Uncomment the line below to see what happens:
# True / False  # you can't divide by zero!
print(True * False)
print(True * True)


# wierd: why is this 200?
print((('aa' == 'aa') + ('bb' == 'bb')) * 100)
# same as:
#  (True + True) * 100
#  (1 + 1) * 100
#  (2) * 100
#  200


# even wierder. Why is this 0? 
print(('aa' == 'aa' + 'bb' == 'bb') * 100) 

# Because addition gets evaluated before comparison operators (reviewed below)
# same as: 
#  ('aa' == ('aa' + 'bb') == 'bb') * 100 
#  ('aa' == 'aabb' == 'bb') * 100
#  (False) * 100
#  (0) * 100
#  0

