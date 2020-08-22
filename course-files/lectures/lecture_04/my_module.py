def get_hypotenuse(side_a: float, side_b: float):
    '''
    Calculates the hypotenuse of a right triangle
    Args: 
        side_a(float): the length of the first side.
        side_b(float): the length of the second side.
    Returns: 
        float: the hypotenuse
    '''
    return (side_a ** 2 + side_b ** 2) ** 0.5

def get_area(side_a: float, side_b: float):
    '''
    Calculates the area of a right triangle
    Args: 
        side_a(float): the length of the first side.
        side_b(float): the length of the second side.
    Returns: 
        float: the area
    '''
    area = (side_a * side_b) / 2
    return area

def get_perimeter(side_a: float, side_b: float):
    '''
    Calculates the perimeter of a right triangle
    Args: 
        side_a(float): the length of the first side.
        side_b(float): the length of the second side.
    Returns: 
        float: the area
    '''
    perimeter = side_a + side_b + get_hypotenuse(side_a, side_b)
    return perimeter

def print_to_2_decimal_places(num: float):
    '''
    Prints a float to two decimal places
    Args: 
        num(float): the number to print
    Returns: 
        Does not return a value
    '''
    num = round(num, ndigits=2)
    print('{0:.2f}'.format(num))
