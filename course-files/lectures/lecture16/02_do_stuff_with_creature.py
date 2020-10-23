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

# note that I'm tagging the creatures:
creature.make_creature(canvas, (200, 200), size=150, tag='creature_1', fill='#f0a202')
creature.make_creature(canvas, (100, 400), size=50, tag='creature_2', fill='#f18805')
creature.make_creature(canvas, (50, 400), size=75, tag='creature_3', fill='#f0a202')
creature.make_creature(canvas, (400, 100), size=250, tag='creature_4', fill='#d95d39')
creature.make_creature(canvas, (350, 350), size=150, tag='creature_5', fill='#7b9e89')

palette = ['#f0a202', '#f18805', '#d95d39', '#0e1428', '#7b9e89']

# Your job: animate only creature 1 and 4...


########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()