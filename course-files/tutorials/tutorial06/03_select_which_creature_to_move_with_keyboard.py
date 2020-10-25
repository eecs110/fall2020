from tkinter import Canvas, Tk
import random
import time
import creature
import utilities
import math

gui = Tk()
gui.title('Circle')
canvas = Canvas(gui, width=500, height=500)
canvas.pack()
canvas.focus_set()
########################## YOUR CODE BELOW THIS LINE ##############################

KEY_PRESS = '<Key>'
MOUSE_CLICK = '<Button-1>'

def select_creature(event):
    tag = utilities.get_tag_from_x_y_coordinate(canvas, event.x, event.y)
    print(tag)

def move_creature(event):
    # update this code so that the code moves the creature who has just
    # been selected by the user.
    print(event.keycode)
    utilities.update_position_by_tag(canvas, 'creature_1', x=10, y=0)


creature.make_creature(canvas, (150, 200), size=100, tag='creature_1')
creature.make_creature(canvas, (350, 200), size=100, tag='creature_2')


canvas.bind(KEY_PRESS, move_creature) 
canvas.bind(MOUSE_CLICK, select_creature) 

########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()