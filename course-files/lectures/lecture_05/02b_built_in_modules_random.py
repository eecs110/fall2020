from tkinter import Canvas, Tk
import random
gui = Tk()
gui.title('Shapes')
canvas = Canvas(gui, width=500, height=300, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

def make_oval(canvas:Canvas, center:tuple, x_radius:int=10, y_radius:int=10, color=None):
    x, y = center
    top_left = (x - x_radius, y - y_radius)
    bottom_right = (x + x_radius, y + y_radius)
    canvas.create_oval([top_left, bottom_right], fill=color)

make_oval(
    canvas, 
    (random.randint(0, 500), random.randint(0, 300)), 
    x_radius=random.randint(10, 200), 
    y_radius=random.randint(10, 200),
    color='hotpink')


########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()