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

############################
# COMPLETED FOR YOU: FRANK #
############################
y = 50
for row in frank:
    # draw each row at the specified (x, y) position:
    draw_row(canvas, row, (50, y), pixel=20)
    # ...and don't forget to shift the y-value down by the proper
    #  amount so that the next row won't draw on top of the first one:
    y += 20


#########################
# STILL TODO: THE HEART #
#########################
draw_row(canvas, heart[0], (250, 250), pixel=10)
draw_row(canvas, heart[1], (250, 260), pixel=10)
draw_row(canvas, heart[2], (250, 270), pixel=10)
draw_row(canvas, heart[3], (250, 280), pixel=10)
draw_row(canvas, heart[4], (250, 290), pixel=10)
draw_row(canvas, heart[5], (250, 300), pixel=10)



########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()