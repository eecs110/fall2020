from tkinter import Canvas, Tk
import time
import shapes
import math

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# Using a while loop, please complete the following:
#   1. Make the circle smoothly move across the screen
#   2. Make it move backwards (on your own)
#   3. Make it move vertically (on your own)
#   4. Make it move diagonally (on your own)
#   5. If it gets to the end, of the screen, 
#      make it reverse directions  (on your own)
#   6. Make it oscillate back and forth  (on your own)

length = 40

# make circle
circle_id = shapes.make_circle(canvas, (60, 60), 50, color='hotpink')

# only animate square rotation thingy 3 times...

counter = 0
num_squares_drawn = 0


counter = 0
while True:
    x1 = round(math.sin(counter), 2)
    x2 = round(math.sin(counter/20), 2)
    x3 = round(math.sin(counter) * 10, 2)
    x4 = round(math.sin(counter/20) * 10, 2)
    print(x1, x2, x3, x4)
    shapes.move(canvas, circle_id, x=x2, y=0)
    gui.update()
    time.sleep(.001)
    counter += 1


##while num_squares_drawn < 3:
##    if counter < 50:
##        # right
##        shapes.move(canvas, circle_id, x=3, y=0)
##    elif counter < 100:
##        # down
##        shapes.move(canvas, circle_id, x=0, y=3)
##    elif counter < 150:
##        # left
##        shapes.move(canvas, circle_id, x=-3, y=0)
##    elif counter < 200:
##        # up
##        shapes.move(canvas, circle_id, x=0, y=-3)
##    else:
##        counter = 0
##        num_squares_drawn += 1
##    counter += 1
##    gui.update()
##    time.sleep(.01)

########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()
