from tkinter import Canvas, Tk
from utilities import make_square, make_grid, get_file_path

# initialize window
gui = Tk()
canvas = Canvas(gui, width=650, height=600, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# helper function that draws a grid.
make_grid(canvas, 650, 600)

def make_row(canvas:Canvas, top_left:tuple, colors:list, palette, pixel:int=10):
    # assume that a list of 9 is always passed in:
    x, y = top_left
    for num in colors:
        if num:
            color = palette[num]
            make_square(canvas, (x, y), pixel, fill_color=color, outline_color='#000')
        x += pixel
   

def draw_pixel_art(
        canvas:Canvas, 
        top_left:tuple, 
        file_name:str, 
        pixel:int=10, 
        palette=(None, '#75B9BE', 'black', 'white')
    ):

    '''
    CHALLENGE:
    1. Open and read the file
    2. Convert each row of the file into a list of ints
    3. Invoke the make_row function for each list of ints as follows:
       make_row(canvas, (x, y), row, pixel=pixel ,palette=palette), where:
       * (x, y) is the top-left coordinate of the drawing
       * row (tuple or list) is a list of color codes that correspond to a row
       * pixel (int) is the size of each pixel
       * palette (tuple or list) is a list or tuple of colors
    4. Don't forget to increment the y after reading each line!
    '''
    


# Invoke your function:
draw_pixel_art(canvas, (120, 220), 'heart.csv', pixel=12, palette=(None, '#E0607E', 'black', 'white'))
draw_pixel_art(canvas, (20, 20), 'flower.csv', palette=(None, 'black', '#FF0000', 'orange', 'yellow', 'white', '#5ec031'))
draw_pixel_art(canvas, (315, 380), 'frank.csv', pixel=15, palette=(None, 'black', '#5ec031', 'white'))

# draw_pixel_art(canvas, (420, 250), 'heart.csv', pixel=8)
# draw_pixel_art(canvas, (55, 415), 'flower.csv', pixel=6, palette=(None, 'black', '#FF0000', 'orange', 'yellow', 'white', '#5ec031'))
# draw_pixel_art(canvas, (350, 115), 'frank.csv', pixel=5, palette=(None, 'black', '#5ec031', 'white'))
# draw_pixel_art(canvas, (420, 10), 'heart.csv', pixel=10, palette=(None, '#E0607E', 'black', 'white'))


########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()