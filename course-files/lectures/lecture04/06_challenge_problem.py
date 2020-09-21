from tkinter import Canvas, Tk
import random

################################################################
gui = Tk()
canvas = Canvas(gui, width=700, height=350, background='white')
canvas.pack()
################################################################
# Your code below this line:



# Each element in the "coordinates" list refers to an (x, y) position 
# (represented as a tuple). The coordinates below draw a square. 
# YOUR TASKS
# 1. Try to make the square twice as big
# 2. Try to make the square half as big
# 3. Try and make a different kind of polygon?
# 4. Try to make the shape turn a different color each time the program is run
#    using the palette tuple and the random.randint function

coordinates = [
    (50, 50),
    (50, 150),
    (150, 150),
    (150, 50)
]
palette = ('#808d8e', '#766c7f', '#947eb0', '#a3a5c3', '#a9d2d5')
canvas.create_polygon(
    coordinates,
    fill='red',
    width=5
)


# Your code above this line:
################################################################
canvas.mainloop()
################################################################