'''
INSTRUCTIONS: Update this function as follows:
If red is turned on, make the background red.
If yellow is turned on, make the background yellow.
If blue is turned on, make the background blue.
If red and yellow are both turned on, make the background orange.
If red and blue are turned on, make the background purple.
If yellow and blue are turned on, make the background green.
If everything is turned on, then make the background black.
'''

def get_color(red_switch:bool, yellow_switch:bool, blue_switch:bool):
    '''
    Given the value of each color switch, this function will return the
    correct color.
    Parameters:
        red_switch(bool): whether red channel is on
        yellow_switch(bool): whether red channel is on
        blue_switch(bool): whether red channel is on
    Returns:
        The color (str) that is produced by the the combination 
        of the colors that are passed in as arguments.
    '''
    if red_switch and yellow_switch and blue_switch:
        return 'black'
    elif red_switch and yellow_switch:
        return 'orange'
    elif red_switch and blue_switch:
        return 'purple'
    elif yellow_switch and blue_switch:
        return 'green'
    elif red_switch:
        return 'red'
    elif blue_switch:
        return 'blue'
    elif yellow_switch:
        return 'yellow'
    else:
        return 'white'

assert get_color(True, True, True) == 'black', 'get_color should return black'
assert get_color(True, True, False) == 'orange', 'get_color should return orange'
assert get_color(True, False, True) == 'purple', 'get_color should return purple'
assert get_color(False, True, True) == 'green', 'get_color should return green'
assert get_color(True, False, False) == 'red', 'get_color should return red'
assert get_color(False, True, False) == 'yellow', 'get_color should return yellow'
assert get_color(False, False, True) == 'blue', 'get_color should return blue'
assert get_color(False, False, False) == 'white', 'get_color should return white'
print('all tests passed')
    

print(get_color(True, True, True))
print(get_color(True, True, False))
print(get_color(True, False, True))
print(get_color(False, True, True))
print(get_color(True, False, False))
print(get_color(False, True, False))
print(get_color(False, False, True))
print(get_color(False, False, False))