from tkinter import Canvas, Tk
from helpers import make_square, make_grid

# initialize window
gui = Tk()
canvas = Canvas(gui, width=600, height=600, background='white')
canvas.pack()

make_grid(canvas, 600, 600)

# HINT 2:
# How could you alter this program so that frank can easily be
# drawn *anywhere on the screen?
#
# Answer: you can always offset the x and y position of each "make_square"
# function call by ADDING the offset to each top_left coordinate argument.
# In other words, in the previous example, there was an implicit offset of
# (0, 0). But you wanted to change this offet to, say, (100, 50), then you
# would always add 100 to the value of your x coordinate and 50 to the
# value of your y coordinate as shown below.
#
# Now, how could you convert the program below to a function so that you
# could create multiple frankensteins drawn at different sizes, colors, and 
# position?

# frankenstein anchored at position (x, y)
pixel = 20
top_left = (100, 50)
body_color = '#5ec031'
pants_color = 'hotpink'
x = top_left[0]
y = top_left[1]

# row 1
make_square(canvas, (x + 2*pixel, y), pixel, fill_color='black')
make_square(canvas, (x + 3*pixel, y), pixel, fill_color='black')
make_square(canvas, (x + 4*pixel, y), pixel, fill_color='black')
make_square(canvas, (x + 5*pixel, y), pixel, fill_color='black')
make_square(canvas, (x + 6*pixel, y), pixel, fill_color='black')

# row 2
make_square(canvas, (x + 2*pixel, y + pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 3*pixel, y + pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 4*pixel, y + pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 5*pixel, y + pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 6*pixel, y + pixel), pixel, fill_color=body_color)

# row 3
make_square(canvas, (x + 2*pixel, y + 2*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 3*pixel, y + 2*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 4*pixel, y + 2*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 5*pixel, y + 2*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 6*pixel, y + 2*pixel), pixel, fill_color=body_color)

# row 4
make_square(canvas, (x + 2*pixel, y + 3*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 3*pixel, y + 3*pixel), pixel, fill_color='black')
make_square(canvas, (x + 4*pixel, y + 3*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 5*pixel, y + 3*pixel), pixel, fill_color='black')
make_square(canvas, (x + 6*pixel, y + 3*pixel), pixel, fill_color=body_color)

# row 5
make_square(canvas, (x + 2*pixel, y + 4*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 3*pixel, y + 4*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 4*pixel, y + 4*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 5*pixel, y + 4*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 6*pixel, y + 4*pixel), pixel, fill_color=body_color)

# row 6
make_square(canvas, (x + 1*pixel, y + 5*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 2*pixel, y + 5*pixel), pixel, fill_color='gray')
make_square(canvas, (x + 3*pixel, y + 5*pixel), pixel, fill_color='gray')
make_square(canvas, (x + 4*pixel, y + 5*pixel), pixel, fill_color='gray')
make_square(canvas, (x + 5*pixel, y + 5*pixel), pixel, fill_color='gray')
make_square(canvas, (x + 6*pixel, y + 5*pixel), pixel, fill_color='gray')
make_square(canvas, (x + 7*pixel, y + 5*pixel), pixel, fill_color=body_color)

# row 7
make_square(canvas, (x + 0*pixel, y + 6*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 1*pixel, y + 6*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 2*pixel, y + 6*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 3*pixel, y + 6*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 4*pixel, y + 6*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 5*pixel, y + 6*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 6*pixel, y + 6*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 7*pixel, y + 6*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 8*pixel, y + 6*pixel), pixel, fill_color=body_color)

# row 8
make_square(canvas, (x + 0*pixel, y + 7*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 1*pixel, y + 7*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 2*pixel, y + 7*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 3*pixel, y + 7*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 4*pixel, y + 7*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 5*pixel, y + 7*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 6*pixel, y + 7*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 7*pixel, y + 7*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 8*pixel, y + 7*pixel), pixel, fill_color=body_color)

# row 9
make_square(canvas, (x + 2*pixel, y + 8*pixel), pixel, fill_color=pants_color)
make_square(canvas, (x + 3*pixel, y + 8*pixel), pixel, fill_color=pants_color)
make_square(canvas, (x + 4*pixel, y + 8*pixel), pixel, fill_color=pants_color)
make_square(canvas, (x + 5*pixel, y + 8*pixel), pixel, fill_color=pants_color)
make_square(canvas, (x + 6*pixel, y + 8*pixel), pixel, fill_color=pants_color)

# row 10
make_square(canvas, (x + 2*pixel, y + 9*pixel), pixel, fill_color=pants_color)
make_square(canvas, (x + 3*pixel, y + 9*pixel), pixel, fill_color=pants_color)
make_square(canvas, (x + 4*pixel, y + 9*pixel), pixel, fill_color=pants_color)
make_square(canvas, (x + 5*pixel, y + 9*pixel), pixel, fill_color=pants_color)
make_square(canvas, (x + 6*pixel, y + 9*pixel), pixel, fill_color=pants_color)

# row 11
make_square(canvas, (x + 2*pixel, y + 10*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 3*pixel, y + 10*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 5*pixel, y + 10*pixel), pixel, fill_color=body_color)
make_square(canvas, (x + 6*pixel, y + 10*pixel), pixel, fill_color=body_color)


########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()