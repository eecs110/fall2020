'''
Documentation: http://effbot.org/tkinterbook/canvas.htm
'''
from tkinter import Canvas, Tk
from helpers import make_grid       # import the make_grid function (for debugging)

gui = Tk()
gui.title('Shapes')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# Your tasks: modify the function bodies of the following 4 function definitions:
#  1. make_oval (Exercise 1)
#  2. make_circle (Exercise 2)
#  3. make_face (Exercise 3)
#  4. make_bullseye (Exercise 4)

########################
# FUNCTION DEFINITIONS #
########################
def make_oval(canvas: Canvas, center: tuple, radius_x: float, radius_y: float, fill: str='hotpink'):
    # Exercise 1: currently, this function creates a hard-coded oval with a top-left
    # coordinate of (100, 100), and a bottom-right coordinate of (200, 150). 
    # 
    # Your job is to modify the code so that:
    # 1. the top-left (x, y) and bottom-right (x, y) coordinates are 
    #    calculated  based on the radius_x, radius_y and center point 
    #    specified by the arguments.
    # 2. the fill color is determined based on the fill argument.
    canvas.create_oval(
        [
            (100, 100), 
            (200, 150)
        ],
        fill='hotpink')



def make_circle(canvas: Canvas, center: tuple, radius: int, fill: str='hotpink'):
    # Exercise 2: currently, this function creates a hard-coded circle with a top-left
    # coordinate of (300, 100), and a bottom-right coordinate of (400, 200). 
    # 
    # Your job is  to modify the code so that:
    # 1.  the top-left (x, y) and bottom-right (x, y) coordinates are 
    #     calculated based on the radius and center point specified 
    #     by arguments.
    # 2.  the fill color is  determined by the fill argument.
    #
    # HINT: complete this taks by calling (or "invoking") the 
    #       make_oval function that you just made in Exercise 1.

    canvas.create_oval(
        [
            (300, 100), 
            (400, 200)
        ],
        fill='hotpink')


def make_face(canvas: Canvas, center: tuple, width: int):
    # Exercise 3: use the make_circle and make_oval functions that you've just
    # created to draw a face. The face should be a circle, and it should have 2
    # oval eyes. The eyes should scale with the width of the face. Replace the
    # "pass" keyword in the function body (below) with your code.
    pass




def make_bullseye(canvas: Canvas, center: tuple, radius: int, distance: int=10):
    # Exercise 4: use the make_circle function that you just created to 
    # draw a bullseye of alternating colors (use any color of your choice).
    #
    # Please ensure that:
    # 1. The smallest  concentric circle has a radius of `radius` 
    #    (value of the argument).
    # 2. Each  additional concentric circle has a radius of `distance` units 
    #    more that the previous  circle.
    #
    # For instance, if `radius`=10 and `distance`=5, then the first circle would have a 
    # radius of 10, the second a radius of 15, the third 20, and the fourth 25.
    #
    # Hint: you'll have to draw the biggest circle first, or else your big circle will
    # overwrite and block the smaller circles. Replace the "pass" keyword in 
    # the function body (below) with your code.
    pass



#####################################
# HOW I WANT TO CALL YOUR FUNCTIONS #
#####################################

# for measuring (optional):
make_grid(canvas, 500, 500)

# Exercise 1: ovals:
print('Exercise 1...')
make_oval(canvas, (100, 100), 25, 40)
make_oval(canvas, (200, 100), 40, 25, fill='navy')
make_oval(canvas, (300, 100), 25, 40, fill='teal')
make_oval(canvas, (400, 100), 40, 25)

# Exercise 2: circles:
print('Exercise 2...')
make_circle(canvas, (100, 200), 25, fill='teal')
make_circle(canvas, (200, 200), 50)
make_circle(canvas, (300, 200), 25, fill='navy')
make_circle(canvas, (400, 200), 50, fill='teal')

# Exercise 3: faces:
print('Exercise 3...')
make_face(canvas, (100, 300), 40)
make_face(canvas, (200, 300), 60)
make_face(canvas, (300, 300), 80)
make_face(canvas, (400, 300), 100)

# Exercise 4: bullseye:
print('Exercise 4...')
make_bullseye(canvas, (100, 400), 5, distance=5)
make_bullseye(canvas, (200, 400), 5, distance=10)
make_bullseye(canvas, (300, 400), 10, distance=5)
make_bullseye(canvas, (400, 400), 20, distance=10)



########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()