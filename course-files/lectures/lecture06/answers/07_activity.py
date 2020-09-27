from operator import add, mul
from math import sqrt
# for more info, see the docs: https://docs.python.org/3/library/operator.html 


def get_area(side_a:float, side_b:float):
    rect_area = mul(side_a, side_b)
    triangle_area = mul(rect_area, 0.5)
    return round(triangle_area, 2)

def get_perimeter(side_a:float, side_b:float):
    side_c = get_hypotenuse(side_a, side_b)
    return round(side_a + side_b + side_c, 2)

def get_hypotenuse(side_a:float, side_b:float):
    sq_a = pow(side_a, 2)
    sq_b = pow(side_b, 2)
    sum_sqa_sqb = add(sq_a, sq_b)
    hypotenuse = sqrt(sum_sqa_sqb)
    return round(hypotenuse, 2)


### Calling / invoking our functions down below:
print('area:', 5, 12, get_area(5, 12))
print('area:', 3, 5, get_area(3, 5))
print('area:', 4, 4, get_area(4, 4))

print('perimeter:', 5, 12, get_perimeter(5, 12))
print('perimeter:', 3, 5, get_perimeter(3, 5))
print('perimeter:', 4, 4, get_perimeter(4, 4))

print('hypotenuse:', 5, 12, get_hypotenuse(5, 12))
print('hypotenuse:', 3, 5, get_hypotenuse(3, 5))
print('hypotenuse:', 4, 4, get_hypotenuse(4, 4))

