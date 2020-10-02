from tkinter import Canvas, Tk
'''
Documentation: http://effbot.org/tkinterbook/canvas.htm
Color Picker: https://coolors.co/
'''

def make_oval(canvas: Canvas, center: tuple, width: int, height: int, fill: str='hotpink'):
    top_left = (center[0] - width, center[1] - height)
    bottom_right = (center[0] + width, center[1] + height)
    canvas.create_oval([top_left, bottom_right], fill=fill)


def make_circle(canvas: Canvas, center: tuple, radius: int, fill: str='hotpink'):
    make_oval(canvas, center, radius, radius, fill=fill)


def make_grid(canvas, w, h):
    interval = 100

    # Delete old grid if it exists:
    canvas.delete('grid_line')
    # Creates all vertical lines at intevals of 100
    for i in range(0, w, interval):
        canvas.create_line(i, 0, i, h, tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, interval):
        canvas.create_line(0, i, w, i, tag='grid_line')

    # Creates axis labels
    offset = 2
    for y in range(0, h, interval):
        for x in range(0, w, interval):
            canvas.create_oval(
                x - offset, 
                y - offset, 
                x + offset,  
                y + offset, 
                fill='black'
            )
            canvas.create_text(
                x + offset, 
                y + offset, 
                text="({0}, {1})".format(x, y),
                anchor="nw", 
                font=("Purisa", 8)
            )
