from tkinter import Canvas, Tk
from helpers import make_square, make_grid

# initialize window
gui = Tk()
canvas = Canvas(gui, width=600, height=600, background='white')
canvas.pack()


# helper function that draws a grid.
make_grid(canvas, 600, 600)

# HINT 1:
# Note that each of the x-positions can be re-written in terms of
# the pixel value. The advantage of rewriting your code in this
# way is that it allows you to be able to scale your frankenstein.
# In other words, if you update the size of the pixel (using the
# pixel variable below), the monster scales.

# However, no matter what, frankenstein is still anchored at
# position (0, 0). How could you alter this program so that frank
# could be drawn *anywhere on the screen?

pixel = 25
body_color = '#5ec031'
pants_color = 'hotpink'


# row 1                                                                        # before: 
make_square(canvas, (2*pixel, 0), pixel, fill_color='black')            # (50, 0), 25
make_square(canvas, (3*pixel, 0), pixel, fill_color='black')            # (75, 0), 25
make_square(canvas, (4*pixel, 0), pixel, fill_color='black')            # (100, 0), 25
make_square(canvas, (5*pixel, 0), pixel, fill_color='black')            # (125, 0), 25
make_square(canvas, (6*pixel, 0), pixel, fill_color='black')            # (150, 0), 25

# row 2
make_square(canvas, (2*pixel, pixel), pixel, fill_color=body_color)     # (50, 25), 25
make_square(canvas, (3*pixel, pixel), pixel, fill_color=body_color)     # (75, 25), 25
make_square(canvas, (4*pixel, pixel), pixel, fill_color=body_color)     # (100, 25), 25
make_square(canvas, (5*pixel, pixel), pixel, fill_color=body_color)     # (125, 25), 25
make_square(canvas, (6*pixel, pixel), pixel, fill_color=body_color)     # (150, 25), 25

# row 3
make_square(canvas, (2*pixel, 2*pixel), pixel, fill_color=body_color)   # (50, 50), 25
make_square(canvas, (3*pixel, 2*pixel), pixel, fill_color=body_color)   # (75, 50), 25
make_square(canvas, (4*pixel, 2*pixel), pixel, fill_color=body_color)   # (100, 50), 25
make_square(canvas, (5*pixel, 2*pixel), pixel, fill_color=body_color)   # (125, 50), 25
make_square(canvas, (6*pixel, 2*pixel), pixel, fill_color=body_color)   # (150, 50), 25

# row 4
make_square(canvas, (2*pixel, 3*pixel), pixel, fill_color=body_color)   # ... (and so forth)
make_square(canvas, (3*pixel, 3*pixel), pixel, fill_color='black')
make_square(canvas, (4*pixel, 3*pixel), pixel, fill_color=body_color)
make_square(canvas, (5*pixel, 3*pixel), pixel, fill_color='black')
make_square(canvas, (6*pixel, 3*pixel), pixel, fill_color=body_color)

# row 5
make_square(canvas, (2*pixel, 4*pixel), pixel, fill_color=body_color)
make_square(canvas, (3*pixel, 4*pixel), pixel, fill_color=body_color)
make_square(canvas, (4*pixel, 4*pixel), pixel, fill_color=body_color)
make_square(canvas, (5*pixel, 4*pixel), pixel, fill_color=body_color)
make_square(canvas, (6*pixel, 4*pixel), pixel, fill_color=body_color)

# row 6
make_square(canvas, (1*pixel, 4*pixel), pixel, fill_color=body_color)
make_square(canvas, (2*pixel, 4*pixel), pixel, fill_color='gray')
make_square(canvas, (3*pixel, 4*pixel), pixel, fill_color='gray')
make_square(canvas, (4*pixel, 4*pixel), pixel, fill_color='gray')
make_square(canvas, (5*pixel, 4*pixel), pixel, fill_color='gray')
make_square(canvas, (6*pixel, 4*pixel), pixel, fill_color='gray')
make_square(canvas, (7*pixel, 4*pixel), pixel, fill_color=body_color)

# row 7
make_square(canvas, (0*pixel, 5*pixel), pixel, fill_color=body_color)
make_square(canvas, (1*pixel, 5*pixel), pixel, fill_color=body_color)
make_square(canvas, (2*pixel, 5*pixel), pixel, fill_color=body_color)
make_square(canvas, (3*pixel, 5*pixel), pixel, fill_color=body_color)
make_square(canvas, (4*pixel, 5*pixel), pixel, fill_color=body_color)
make_square(canvas, (5*pixel, 5*pixel), pixel, fill_color=body_color)
make_square(canvas, (6*pixel, 5*pixel), pixel, fill_color=body_color)
make_square(canvas, (7*pixel, 5*pixel), pixel, fill_color=body_color)
make_square(canvas, (8*pixel, 5*pixel), pixel, fill_color=body_color)

# row 8
make_square(canvas, (0*pixel, 6*pixel), pixel, fill_color=body_color)
make_square(canvas, (1*pixel, 6*pixel), pixel, fill_color=body_color)
make_square(canvas, (2*pixel, 6*pixel), pixel, fill_color=body_color)
make_square(canvas, (3*pixel, 6*pixel), pixel, fill_color=body_color)
make_square(canvas, (4*pixel, 6*pixel), pixel, fill_color=body_color)
make_square(canvas, (5*pixel, 6*pixel), pixel, fill_color=body_color)
make_square(canvas, (6*pixel, 6*pixel), pixel, fill_color=body_color)
make_square(canvas, (7*pixel, 6*pixel), pixel, fill_color=body_color)
make_square(canvas, (8*pixel, 6*pixel), pixel, fill_color=body_color)

# row 9
make_square(canvas, (2*pixel, 7*pixel), pixel, fill_color=pants_color)
make_square(canvas, (3*pixel, 7*pixel), pixel, fill_color=pants_color)
make_square(canvas, (4*pixel, 7*pixel), pixel, fill_color=pants_color)
make_square(canvas, (5*pixel, 7*pixel), pixel, fill_color=pants_color)
make_square(canvas, (6*pixel, 7*pixel), pixel, fill_color=pants_color)

# row 10
make_square(canvas, (2*pixel, 8*pixel), pixel, fill_color=pants_color)
make_square(canvas, (3*pixel, 8*pixel), pixel, fill_color=pants_color)
make_square(canvas, (4*pixel, 8*pixel), pixel, fill_color=pants_color)
make_square(canvas, (5*pixel, 8*pixel), pixel, fill_color=pants_color)
make_square(canvas, (6*pixel, 8*pixel), pixel, fill_color=pants_color)

# row 11
make_square(canvas, (2*pixel, 9*pixel), pixel, fill_color=body_color)
make_square(canvas, (3*pixel, 9*pixel), pixel, fill_color=body_color)
make_square(canvas, (5*pixel, 9*pixel), pixel, fill_color=body_color)
make_square(canvas, (6*pixel, 9*pixel), pixel, fill_color=body_color)



########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()