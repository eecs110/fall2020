from tkinter import Canvas, Tk
import helpers

# initialize window
gui = Tk()
canvas = Canvas(gui, width=700, height=350, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

canvas.create_oval(
    [(100, 100), (200, 200)], #top right (x, y) and bottom left (x, y)
    fill='hotpink',
    width=5
)

canvas.create_oval(
    [(200, 100), (300, 200)],
    fill='teal',
    width=5
)

helpers.make_grid(canvas, 700, 350)

########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()