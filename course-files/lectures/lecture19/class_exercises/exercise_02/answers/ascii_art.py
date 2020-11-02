from tkinter import Canvas, Tk
from utilities import make_square, make_grid, get_file_path

# initialize window
gui = Tk()
canvas = Canvas(gui, width=650, height=600, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# helper function that draws a grid.
make_grid(canvas, 650, 600)

'''
CHALLENGE:
Create a function called draw_pixel_art that: 
1. Opens and reads the file (passed into the function)
2. Convert each row of the file into a list of ints
3. Draws a square for each pixel row and column
'''

def draw_pixel_art(canvas:Canvas, top_left:tuple, file_name:str, pixel:str=10,
        palette=(None, '#75B9BE', 'black', 'white')):
    x_original = top_left[0] 
    x = top_left[0]
    y = top_left[1]
    f = open(get_file_path(file_name), 'r')
    
    # for outputting each row
    for line in f.readlines():
        pixel_strings = line.split(',')

        # for outputting each cell (for the row):
        for num_string in pixel_strings:
            num = int(num_string)
            color = palette[num]
            if color is not None:
                make_square(canvas, (x, y), pixel, fill_color=color, outline_color='#000')
            x += pixel
        
        # increment the y and reset the x when you're about to move 
        # to a new row
        y += pixel
        x = x_original




# Invoke your function:
draw_pixel_art(canvas, (0, 20), file_name='flower.csv', palette=(None, 'black', '#FF0000', 'orange', 'yellow', 'white', '#5ec031'))
draw_pixel_art(canvas, (120, 220), file_name='heart.csv', pixel=12, palette=(None, '#E0607E', 'black', 'white'))
draw_pixel_art(canvas, (420, 250), file_name='heart.csv', pixel=8)
draw_pixel_art(canvas, (55, 415), pixel=6, file_name='flower.csv', palette=(None, 'black', '#FF0000', 'orange', 'yellow', 'white', '#5ec031'))
draw_pixel_art(canvas, (350, 115), pixel=5, file_name='frank.csv', palette=(None, 'black', '#5ec031', 'white'))
draw_pixel_art(canvas, (315, 380), pixel=15, file_name='frank.csv', palette=(None, 'black', '#5ec031', 'white'))
draw_pixel_art(canvas, (420, 10), file_name='heart.csv', pixel=10, palette=(None, '#E0607E', 'black', 'white'))


########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()