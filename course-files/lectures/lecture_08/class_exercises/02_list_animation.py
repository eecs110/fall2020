from tkinter import Canvas, Tk
import time
import shapes
import math

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

shapes.make_circle(canvas, (60, 60), 10, color=None, tag='circle1')
shapes.make_circle(canvas, (200, 30), 20, color=None, tag='circle2')
shapes.make_circle(canvas, (330, 10), 10, color=None, tag='circle3')
shapes.make_circle(canvas, (520, 40), 15, color=None, tag='circle4')

# only animate square rotation thingy 3 times...

counter = 0
num_squares_drawn = 0


counter = 0
while True:
    shapes.move(canvas, 'circle1', x=0, y=3)
    gui.update()
    time.sleep(.001)
    counter += 1

########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()
