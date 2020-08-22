from operator import add, mul, sub, truediv, mod, floordiv, pow
# for more info, see the docs: https://docs.python.org/3/library/operator.html 

# Challenge:
# write a program to calculate the hypotenuse of a right triangle
# if the first side is 5 and the second side is 12. You may not 
# use operators. You must use the functions imported above:
# add(1, 2)     -> returns 3
# pow(5, 2)     -> returns 25
# pow(25, 0.5)  -> returns 5

side_a = 5
side_b = 12

# approach 1: break it into steps -- might be easier to read and understand:
sq_side_a = pow(side_a, 2)
sq_side_b = pow(side_b, 2)
sum_sq_sides = add(sq_side_a, sq_side_b)
sqrt_sum_sq_sides = pow(sum_sq_sides, 0.5)
print(sqrt_sum_sq_sides)

# approach 2: nest all of the functions -- arguably less readable, 
# but also valid 
sqrt_sum_sq_sides = pow(add(pow(side_a, 2), pow(side_b, 2)), 0.5)
print(sqrt_sum_sq_sides)

