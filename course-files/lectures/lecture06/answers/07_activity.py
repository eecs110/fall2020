from operator import add, mul, sub, truediv, mod, floordiv, pow
# for more info, see the docs: https://docs.python.org/3/library/operator.html 

# Challenge: Create a custom function called "hypotenuse" that calculates 
# the hypotenuse of any triangle. Then, invoke that function using the 
# following triangle dimensions:
#    triangle 1: side_a = 5, side_b = 12
#    triangle 2: side_a = 3, side_b = 5
#    triangle 3: side_a = 4, side_b = 4

def hypotenuse(side_a: float, side_b: float):
    return pow(add(pow(side_a, 2), pow(side_b, 2)), 0.5)


print(hypotenuse(5, 12))
print(hypotenuse(3, 5))
print(hypotenuse(4, 4))



#--------------------------------------------------------------------
# FYI (not required): 
#   To format your number so that it only prints to 2 decimal places,
#   you can write a formatting function. We will be going over string 
#   methods later in the course.
#--------------------------------------------------------------------

def print_to_2_decimal_places(num: float):
    num = round(num, ndigits=2)
    print('{0:.2f}'.format(num))

print_to_2_decimal_places(hypotenuse(5, 12))
print_to_2_decimal_places(hypotenuse(3, 5))
print_to_2_decimal_places(hypotenuse(4, 4))
