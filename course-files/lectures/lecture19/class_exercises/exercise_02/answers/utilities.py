from tkinter import Canvas

def _set_coordinates(canvas, id, coordinates):
    canvas.coords(id, coordinates)

def _get_coordinates(canvas, id):
    return canvas.coords(id)

def _get_x_coordinates(canvas, tag):
    return _get_coordinates_by_dimension(canvas, tag, dimension='x')

def _get_y_coordinates(canvas, tag):
    return _get_coordinates_by_dimension(canvas, tag, dimension='y')

def _get_coordinates_by_dimension(canvas, tag, dimension='x'):
    '''
    updates the x and y position of all shapes that have been tagged
    with the tag argument
    '''
    if dimension == 'x':
        pos = 0
    else:
        pos = 1
    shape_ids = canvas.find_withtag(tag)
    coords = []
    for id in shape_ids:
        shape_coords = _get_coordinates(canvas, id)
        for i in range(0, len(shape_coords)):
            if i % 2 == pos:
                coords.append(shape_coords[i])
    return coords

def flip(canvas, tag):
    center = get_center(canvas, tag)
    width = get_width(canvas, tag)
    shape_ids = canvas.find_withtag(tag)
    for shape_id in shape_ids:
        flipped_coordinates = []
        shape_coords = _get_coordinates(canvas, shape_id)
        counter = 0
        for num in shape_coords:
            if counter % 2 == 0:
                flipped_coordinates.append(-num + center[0] + width/2 )
            else:
                flipped_coordinates.append(num)
            counter += 1
        _set_coordinates(canvas, shape_id, flipped_coordinates)

def get_left(canvas, tag):
    '''
    returns the left boundary of the shape group
    '''
    return min(*_get_x_coordinates(canvas, tag))

def get_right(canvas, tag):
    '''
    returns the right boundary of the shape group
    '''
    return max(*_get_x_coordinates(canvas, tag))

def get_top(canvas, tag):
    '''
    returns the top boundary of the shape group
    '''
    return min(*_get_y_coordinates(canvas, tag))

def get_bottom(canvas, tag):
    '''
    returns the bottom boundary of the shape group
    '''
    return max(*_get_y_coordinates(canvas, tag))


def get_width(canvas, tag):
    '''
    returns the width of the shape group
    '''
    x_coords = _get_x_coordinates(canvas, tag)
    return max(*x_coords) - min(*x_coords)

def get_height(canvas, tag):
    '''
    returns the height of the shape group
    '''
    y_coords = _get_y_coordinates(canvas, tag)
    return max(*y_coords) - min(*y_coords)

def get_center(canvas, tag):
    x = get_width(canvas, tag) / 2 + get_left(canvas, tag)
    y = get_height(canvas, tag) / 2 + get_top(canvas, tag)
    return (x, y)


def make_square(canvas: Canvas,top_left: tuple,width: int,fill_color: str='#84A9C0',outline_color='#DDD'):
    canvas.create_rectangle([
            (top_left, # top_left
            top_left[0] + width,top_left[1] + width)  # bottom_right
        ],
        fill=fill_color,
        outline=outline_color
    )


def make_grid(c,w,h):
    interval = 100

    # Delete old grid if it exists:
    c.delete('grid_line')
    # Creates all vertical lines at intevals of 100
    for i in range(0,w,interval):
        c.create_line(i,0,i,h,tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0,h,interval):
        c.create_line(0,i,w,i,tag='grid_line')

    # Creates axis labels
    offset = 2
    for y in range(0,h,interval):
        for x in range(0,w,interval):
            c.create_oval(
                x - offset,
                y - offset,
                x + offset, 
                y + offset,
                fill='black'
            )
            c.create_text(
                x + offset,
                y + offset,
                text="({0},{1})".format(x,y),
                anchor="nw",
                font=("Purisa",8)
            )


def get_file_path(
    file_name, subdirectory=None):
    import os
    import sys
    dir_path = os.path.dirname(sys.argv[0])
    if subdirectory:
        return os.path.join(dir_path, subdirectory, file_name)
    else:
        return os.path.join(dir_path, file_name)
