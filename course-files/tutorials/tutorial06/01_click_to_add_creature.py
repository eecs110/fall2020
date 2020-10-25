from tkinter import Canvas, Tk
import random
import time
import creature
import utilities

gui = Tk()
gui.title('Circle')
canvas = Canvas(gui, width=500, height=500)
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################
MOUSE_CLICK = '<Button-1>'
MOUSE_DRAG = '<B1-Motion>'

# note that I'm assigning each creature a unique tag:
creature.make_creature(canvas, (200, 200), size=150, tag='creature_1', fill='white')
creature.make_creature(canvas, (400, 400), size=120, tag='creature_2')


# your job:
# 1. modify the add_new_creature function so that it
#    adds a new creature at the position where the user clicks.
# 2. Make the size and color of the creature random
# 3. Instead of it using the smiley face, make it work with *your creature
def add_new_creature(event):
    print(event.x, event.y)

canvas.bind(MOUSE_CLICK, add_new_creature) 

########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()