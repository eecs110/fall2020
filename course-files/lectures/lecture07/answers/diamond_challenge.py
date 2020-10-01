from tkinter import Canvas, Tk
from helpers import make_grid

# initialize window
gui = Tk()
canvas = Canvas(gui, width=700, height=550, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

def create_diamond(canvas, 
    center:tuple, size:int=100, fill_color='teal', 
    border_width=5, border_color='black'):
    x = center[0]
    y = center[1]
    radius = size / 2
    canvas.create_polygon(
        [ 
            (x, y - radius), # top-most coordinate
            (x + radius, y), # right-most coordinate
            (x, y + radius), # bottom-most coordinate
            (x - radius, y)  # left-most coordinate
        ],
        fill=fill_color,
        width=border_width,
        outline=border_color,
        activefill='hotpink',
        activeoutline='#999999'
    )
def four_diamonds(canvas, center, size=200, fill_color='teal'):
    diamond_size = size / 2
    radius = diamond_size / 2
    x, y = center
    create_diamond(canvas, (x, y - radius), diamond_size, fill_color=fill_color)
    create_diamond(canvas, (x + radius, y), diamond_size, fill_color=fill_color)
    create_diamond(canvas, (x, y + radius), diamond_size, fill_color=fill_color)
    create_diamond(canvas, (x - radius, y), diamond_size, fill_color=fill_color)

def sixteen_diamonds(canvas, center, size=200, fill_color='teal'):
    diamond_size = size / 2
    radius = diamond_size / 2
    x, y = center
    four_diamonds(canvas, (x, y - radius), diamond_size, fill_color=fill_color)
    four_diamonds(canvas, (x + radius, y), diamond_size, fill_color=fill_color)
    four_diamonds(canvas, (x, y + radius), diamond_size, fill_color=fill_color)
    four_diamonds(canvas, (x - radius, y), diamond_size, fill_color=fill_color)


# invoke your functions:
make_grid(canvas, 700, 550) # just for seeing grid lines

create_diamond(canvas, (100, 400), 100, fill_color='yellow')

four_diamonds(canvas, (200, 200), size=300, fill_color='hotpink')

sixteen_diamonds(canvas, (550, 275), size=200, fill_color='teal')



########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()