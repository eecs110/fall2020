from tkinter import Canvas, Tk
import random
gui = Tk()
gui.title('Shapes')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
palette = ['hotpink', 'yellow', 'teal', 'purple', 'blue', 'pink']

def make_oval(canvas:Canvas, center:tuple, x_radius:int=10, y_radius:int=10, color=None):
    x, y = center
    top_left = (x - x_radius, y - y_radius)
    bottom_right = (x + x_radius, y + y_radius)
    canvas.create_oval([top_left, bottom_right], fill=color)

make_oval(
    canvas, 
    (random.randint(0, 400), random.randint(0, 400)), 
    x_radius=random.randint(10, 100), 
    y_radius=random.randint(10, 100),
    color=random.choice(palette)
)

make_oval(
    canvas, 
    (random.randint(0, 400), random.randint(0, 400)), 
    x_radius=random.randint(10, 100), 
    y_radius=random.randint(10, 100),
    color=random.choice(palette)
)

make_oval(
    canvas, 
    (random.randint(0, 400), random.randint(0, 400)), 
    x_radius=random.randint(10, 100), 
    y_radius=random.randint(10, 100),
    color=random.choice(palette)
)



########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()