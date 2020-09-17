from tkinter import Canvas, Tk
import helpers

# initialize window
gui = Tk()
canvas = Canvas(gui, width=500, height=300, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

canvas.create_polygon([
        (200, 100),  # first coord
        (200, 200),  # second coord
        (300, 200)   # third coord
    ],
    fill='#84A9C0'
)

# helper function that draws a grid.
helpers.make_grid(canvas, 500, 500)

########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()