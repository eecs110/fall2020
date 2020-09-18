from tkinter import Canvas, Tk
from helpers import make_square, make_grid

# initialize window
gui = Tk()
canvas = Canvas(gui, width=600, height=600, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# helper function that draws a grid.
make_grid(canvas, 600, 600)

body_color = '#5ec031'

# row 1
make_square(canvas, (50, 0), 25, fill_color='black')                 # pixel (3, 1)
make_square(canvas, (75, 0), 25, fill_color='black')                 # pixel (4, 1)
make_square(canvas, (100, 0), 25, fill_color='black')                # pixel (5, 1)
make_square(canvas, (125, 0), 25, fill_color='black')                # pixel (6, 1)
make_square(canvas, (150, 0), 25, fill_color='black')                # pixel (7, 1)

# row 2
make_square(canvas, (50, 25), 25, fill_color=body_color)             # pixel (3, 2)
make_square(canvas, (75, 25), 25, fill_color=body_color)             # pixel (4, 2)
make_square(canvas, (100, 25), 25, fill_color=body_color)            # pixel (5, 2)
make_square(canvas, (125, 25), 25, fill_color=body_color)            # pixel (6, 2)
make_square(canvas, (150, 25), 25, fill_color=body_color)            # pixel (7, 2)

# row 3
make_square(canvas, (50, 50), 25, fill_color=body_color)             # pixel (3, 3)
make_square(canvas, (75, 50), 25, fill_color=body_color)             # pixel (4, 3)
make_square(canvas, (100, 50), 25, fill_color=body_color)            # pixel (5, 3)
make_square(canvas, (125, 50), 25, fill_color=body_color)            # pixel (6, 3)
make_square(canvas, (150, 50), 25, fill_color=body_color)            # pixel (7, 3)

# row 4
make_square(canvas, (50, 75), 25, fill_color=body_color)             # pixel (3, 4)
make_square(canvas, (75, 75), 25, fill_color='black')                # pixel (4, 4)
make_square(canvas, (100, 75), 25, fill_color=body_color)            # pixel (5, 4)
make_square(canvas, (125, 75), 25, fill_color='black')               # pixel (6, 4)
make_square(canvas, (150, 75), 25, fill_color=body_color)            # pixel (7, 4)

# row 5
make_square(canvas, (50, 100), 25, fill_color=body_color)            # pixel (3, 5)
make_square(canvas, (75, 100), 25, fill_color=body_color)            # pixel (4, 5)
make_square(canvas, (100, 100), 25, fill_color=body_color)           # pixel (5, 5)
make_square(canvas, (125, 100), 25, fill_color=body_color)           # pixel (6, 5)
make_square(canvas, (150, 100), 25, fill_color=body_color)           # pixel (7, 5)

# row 6
make_square(canvas, (25, 100), 25, fill_color=body_color)            # pixel (2, 6)
make_square(canvas, (50, 100), 25, fill_color='gray')                # pixel (3, 6)
make_square(canvas, (75, 100), 25, fill_color='gray')                # pixel (4, 6)
make_square(canvas, (100, 100), 25, fill_color='gray')               # pixel (5, 6)
make_square(canvas, (125, 100), 25, fill_color='gray')               # pixel (6, 6)
make_square(canvas, (150, 100), 25, fill_color='gray')               # pixel (7, 6)
make_square(canvas, (175, 100), 25, fill_color=body_color)           # pixel (8, 6)

# row 7
make_square(canvas, (0, 125), 25, fill_color=body_color)             # pixel (1, 7)
make_square(canvas, (25, 125), 25, fill_color=body_color)            # pixel (2, 7)
make_square(canvas, (50, 125), 25, fill_color=body_color)            # pixel (3, 7)
make_square(canvas, (75, 125), 25, fill_color=body_color)            # pixel (4, 7)
make_square(canvas, (100, 125), 25, fill_color=body_color)           # pixel (5, 7)
make_square(canvas, (125, 125), 25, fill_color=body_color)           # pixel (6, 7)
make_square(canvas, (150, 125), 25, fill_color=body_color)           # pixel (7, 7)
make_square(canvas, (175, 125), 25, fill_color=body_color)           # pixel (8, 7)
make_square(canvas, (200, 125), 25, fill_color=body_color)           # pixel (9, 7)

# row 8
make_square(canvas, (0, 150), 25, fill_color=body_color)             # pixel (1, 8)
make_square(canvas, (25, 150), 25, fill_color=body_color)            # pixel (2, 8)
make_square(canvas, (50, 150), 25, fill_color=body_color)            # pixel (3, 8)
make_square(canvas, (75, 150), 25, fill_color=body_color)            # pixel (4, 8)
make_square(canvas, (100, 150), 25, fill_color=body_color)           # pixel (5, 8)
make_square(canvas, (125, 150), 25, fill_color=body_color)           # pixel (6, 8)
make_square(canvas, (150, 150), 25, fill_color=body_color)           # pixel (7, 8)
make_square(canvas, (175, 150), 25, fill_color=body_color)           # pixel (8, 8)
make_square(canvas, (200, 150), 25, fill_color=body_color)           # pixel (9, 8)

# row 9
make_square(canvas, (50, 175), 25, fill_color='black')               # pixel (3, 9)
make_square(canvas, (75, 175), 25, fill_color='black')               # pixel (4, 9)
make_square(canvas, (100, 175), 25, fill_color='black')              # pixel (5, 9)
make_square(canvas, (125, 175), 25, fill_color='black')              # pixel (6, 9)
make_square(canvas, (150, 175), 25, fill_color='black')              # pixel (7, 9)

# row 10
make_square(canvas, (50, 200), 25, fill_color='black')               # pixel (3, 10)
make_square(canvas, (75, 200), 25, fill_color='black')               # pixel (4, 10)
make_square(canvas, (100, 200), 25, fill_color='black')              # pixel (5, 10)
make_square(canvas, (125, 200), 25, fill_color='black')              # pixel (6, 10)
make_square(canvas, (150, 200), 25, fill_color='black')              # pixel (7, 10)

# row 11
make_square(canvas, (50, 225), 25, fill_color=body_color)            # pixel (3, 11)
make_square(canvas, (75, 225), 25, fill_color=body_color)            # pixel (4, 11)
make_square(canvas, (125, 225), 25, fill_color=body_color)           # pixel (6, 11)
make_square(canvas, (150, 225), 25, fill_color=body_color)           # pixel (7, 11)













'''

# After you're done making your "make_frank" function, invoke it as follows:
make_frank(canvas, (0, 20))
make_frank(canvas, (180, 220), pixel=20, body_color='#75B9BE')
make_frank(canvas, (420, 250), body_color='#E0607E', pixel=10)
make_frank(canvas, (55, 415), body_color='#B7CE63', pixel=15)
make_frank(canvas, (350, 115), pixel=5, body_color='#75B9BE')
make_frank(canvas, (420, 400), body_color='#E5F77D', pants_color='#75B9BE', pixel=15)
make_frank(canvas, (420, 10), pixel=15)
'''

########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()