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

for y in range(0, 251, 50): #recall that the range function excludes the endpoint
    make_circle(canvas, (100, y), 25)

# another option:
# for y in range(5):
#     make_circle(canvas, (100, y * 50), 25)



########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()