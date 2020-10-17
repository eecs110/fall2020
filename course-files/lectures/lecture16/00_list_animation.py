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

for i in range(0, 100):
    x = random.randint(0, 500) 
    y = random.randint(0, 500)
    rad = random.randint(1, 8)
    tag_name = 'circle_' + str(i)
    shapes.make_circle(canvas, (x, y), rad, color=None, tag=tag_name)


while True:
    for i in range(0, 100):
        tag_name = 'circle_' + str(i)
        shapes.move(canvas, tag_name, x=0, y=3)
    gui.update()
    time.sleep(.001)

########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()
