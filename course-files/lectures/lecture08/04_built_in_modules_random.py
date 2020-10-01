from tkinter import Canvas, Tk
import random
gui = Tk()
gui.title('Shapes')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
palette = ['royalblue', 'cornflowerblue', 'lightsteelblue', 'mistyrose', 'lightsalmon', 'tomato']

def make_random_oval(canvas:Canvas):
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    x_radius=random.randint(10, 100)
    y_radius=random.randint(10, 100)
    top_left = (x - x_radius, y - y_radius)
    bottom_right = (x + x_radius, y + y_radius)
    canvas.create_oval(
        [top_left, bottom_right], 
        fill=random.choice(palette)
    )

make_random_oval(canvas)
make_random_oval(canvas)
make_random_oval(canvas)
make_random_oval(canvas)
make_random_oval(canvas)
make_random_oval(canvas)

########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()