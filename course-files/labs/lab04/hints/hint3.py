from tkinter import Canvas, Tk
from helpers import make_square, make_grid

# initialize window
gui = Tk()
canvas = Canvas(gui, width=600, height=600, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
heart = (
    (0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0),
    (0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 2, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 1, 1, 1),
    (1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1),
    (1, 1, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0),
    (0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
    (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0)
)

frank = (
    (0, 0, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 2, 2, 2, 2, 2, 0, 0),
    (0, 0, 2, 2, 2, 2, 2, 0, 0),
    (0, 0, 2, 1, 2, 1, 2, 0, 0),
    (0, 0, 2, 2, 2, 2, 2, 0, 0),
    (0, 2, 3, 3, 3, 3, 3, 2, 0),
    (0, 2, 2, 2, 2, 2, 2, 2, 0),
    (0, 2, 2, 2, 2, 2, 2, 2, 0),
    (0, 0, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 2, 2, 0, 2, 2, 0, 0)
)



# helper function that draws a grid.
make_grid(canvas, 600, 600)

def draw_row(canvas:Canvas, row:tuple, top_left:tuple, pixel:int=25):
    x = top_left[0]
    y = top_left[1]
    for cell in row:
        if cell == 1:
            make_square(canvas, (x, y), pixel, fill_color='#E0607E')
        elif cell == 2:
            make_square(canvas, (x, y), pixel, fill_color='black')
        elif cell == 3:
            make_square(canvas, (x, y), pixel, fill_color='white')
        x += pixel

# create function:
def draw_pixel_art(canvas:Canvas, top_left:tuple, grid:tuple, pixel:int=10):
    x = top_left[0]
    y = top_left[1]
    for row in grid:
        # draw each row at the specified (x, y) position:
        draw_row(canvas, row, (x, y), pixel=pixel)
        
        # ...and don't forget to shift the y-value down by the proper
        #  amount so that the next row won't draw on top of the first one:
        y += pixel

# invoke function:
draw_pixel_art(canvas, (0, 20), heart)
draw_pixel_art(canvas, (120, 220), frank, pixel=12)
draw_pixel_art(canvas, (420, 250), heart, pixel=8)
draw_pixel_art(canvas, (55, 415), heart, pixel=6)
draw_pixel_art(canvas, (350, 115), heart, pixel=5)
draw_pixel_art(canvas, (315, 380), frank, pixel=15)
draw_pixel_art(canvas, (420, 10), frank, pixel=10)

########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()