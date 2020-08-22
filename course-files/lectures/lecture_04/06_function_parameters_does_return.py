# --------------------------------------------------------
# 4. functions with required parameters and a return value
# --------------------------------------------------------
# function definition:
def add_em(num_1: float, num_2: float):
    '''
    Adds two numbers together.
    Args: 
        num_1(float): the first number in the addition operation.
        num_2(float): the second number in the addition operation.
    Returns: 
        float: the sum of the two numbers
    '''
    return num_1 + num_2

# function call
result = add_em(33, 44)
print('The sum is:', result)
result = add_em(3, 55)
print('The sum is:', result)