from tkinter import Canvas, Tk
import random

gui = Tk()
gui.title('Circle')
# initialize canvas:
canvas = Canvas(gui, width=500, height=500)
canvas.pack()

def make_circle(canvas, center, radius, color='white', tag=None, stroke_width=1, outline=None):
    x, y = center
    canvas.create_oval(
        [ x - radius, y - radius, x + radius, y + radius ],
        fill=color,
        width=stroke_width,
        tags=tag,
        outline=outline
    )
########################## YOUR CODE BELOW THIS LINE ##############################

# Rewrite this code using a loop (any loop you want).
# Your code should only include ONE make_circle function call.
make_circle(canvas, (100, 0), 25)
make_circle(canvas, (100, 50), 25)
make_circle(canvas, (100, 100), 25)
make_circle(canvas, (100, 150), 25)
make_circle(canvas, (100, 200), 25)
make_circle(canvas, (100, 250), 25)



########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()