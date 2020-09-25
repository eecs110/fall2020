from tkinter import Canvas, Tk
from helpers import make_grid

'''
INSTRUCTIONS:
1. Write a program that prompts the user for a color, which can be any string representation of a color
2. Then, draw a rectangle (of any dimensions) with that color
'''


# initialize window
window = Tk()
canvas = Canvas(window, width=700, height=350, background='white')
canvas.pack()
# end initialization code




canvas.create_rectangle(
    [ (100, 25), (250, 75) ],  #  coords: top-left, bottom-right
    fill='purple')





make_grid(canvas, 700, 350)

# don't delete this line:
canvas.mainloop()

