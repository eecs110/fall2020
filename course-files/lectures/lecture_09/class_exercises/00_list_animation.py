from tkinter import Canvas, Tk
import time
import shapes
import math
import random

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################
palette = ('#808d8e', '#766c7f', '#947eb0', '#a3a5c3', '#a9d2d5')


# BUILDING A DATASET (A DATASET OF BUBBLES)
# 50 ROWS OF BUBBLES WHERE THE FIRST CELL IS THE NAME OF
# THE BUBBLE AND THE SECOND CELL IS THE SPEED OF THE BUBBLE
bubbles = []
for i in range(0, 50):
    x = random.randint(0, 500) 
    y = random.randint(0, 500)
    rad = random.randint(1, 8)
    tag_name = 'circle_' + str(i)
    shapes.make_circle(
        canvas,
        (x, y),
        rad,
        color=random.choice(palette),
        tag=tag_name
    )

    bubbles.append([tag_name, random.randint(2, 6)])

for bubble in bubbles:
    print(bubble)

while True:
    # each time the screen redraws (gui.update()), each circle
    # moves by 3 units in the y direction.
    for entry in bubbles:
        tag = entry[0]
        speed = entry[1]
        shapes.move(canvas, tag, x=0, y=speed)
    gui.update()
    time.sleep(.01)

########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()
