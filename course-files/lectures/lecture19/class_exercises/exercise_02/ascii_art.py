from tkinter import Canvas, Tk
from utilities import make_square, make_grid, get_file_path

# initialize window
gui = Tk()
canvas = Canvas(gui, width=650, height=600, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# helper function that draws a grid.
make_grid(canvas, 650, 600)
make_square(canvas, (100, 100), 25, fill_color='teal', outline_color='#000')

'''
CHALLENGE:
Create a function called draw_pixel_art that: 
1. Opens and reads the file (passed into the function)
2. Convert each row of the file into a list of ints
3. Draws a square for each pixel row and column
'''

def draw_pixel_art(canvas:Canvas, top_left:tuple, file_name:str, pixel:str=10):
    pass
    





# Invoke your function:
draw_pixel_art(canvas, (120, 220), 'heart.csv', pixel=12)
# draw_pixel_art(canvas, (20, 20), 'flower.csv')
# draw_pixel_art(canvas, (315, 380), 'frank.csv', pixel=15)


########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()