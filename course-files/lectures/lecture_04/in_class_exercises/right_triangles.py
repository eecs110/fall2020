'''
Part 1: Create a module called right_triangles.py that has three functions:
get_area
get_perimeter
get_hypotenuse
Each of these functions accepts two arguments: side_a (a float) and side_b (also a float), and returns a number corresponding to the calculation.

'''

def get_area(side_a:float, side_b:float):
    return round((side_a * side_b) / 2, 2)

def get_perimeter(side_a:float, side_b:float):
    return round(side_a + side_b + get_hypotenuse(side_a, side_b), 2)

def get_hypotenuse(side_a:float, side_b:float):
    side_a_sq = side_a ** 2
    side_b_sq = side_b ** 2
    return round((side_a_sq + side_b_sq) ** 0.5, 2)



