from tkinter import Canvas, Tk
from helpers import make_grid
from creature import make_creature

# initialize window
gui = Tk()
gui.title('Creature')
canvas = Canvas(gui, width=550, height=550, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################


# Call your creature function with different arguments here:
make_creature(canvas)
make_grid(canvas, 550, 550)


########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()
