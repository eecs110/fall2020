from tkinter import Canvas, Tk
import random

gui = Tk()
gui.title('Circle')
canvas = Canvas(gui, width=500, height=500)
canvas.pack()

def make_rect(canvas, center, radius, color='white', tag=None, stroke_width=1, outline=None):
    x, y = center
    canvas.create_rectangle(
        [ x - radius, y - radius, x + radius, y + radius ],
        fill=color,
        width=stroke_width,
        tags=tag,
        outline=outline
    )
########################## YOUR CODE BELOW THIS LINE ##############################

palette = ['#f0a202', '#f18805', '#d95d39', '#0e1428', '#7b9e89']
# use the range function to make 100 randomly positioned squares: 

make_rect(canvas, (100, 50), 25)
make_rect(canvas, (100, 100), 25)
make_rect(canvas, (100, 150), 25)
make_rect(canvas, (100, 200), 25)
make_rect(canvas, (100, 250), 25)
make_rect(canvas, (100, 300), 25)



########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()