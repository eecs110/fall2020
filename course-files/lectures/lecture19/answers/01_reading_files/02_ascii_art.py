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
        file_name='heart.csv', 
        pixel:int=10, 
        palette=(None, '#75B9BE', 'black', 'white')
    ):
    x = top_left[0]
    y = top_left[1]
    
    f = open(get_file_path(file_name))
    for line in f.readlines():
        row = []
        cells = line.split(',')
        for cell in cells:
            row.append(int(cell))
        make_row(canvas, (x, y), row, palette=palette, pixel=pixel)
        y += pixel


# Invoke your function:
draw_pixel_art(canvas, (0, 20), file_name='flower.csv', palette=(None, 'black', '#FF0000', 'orange', 'yellow', 'white', '#5ec031'))
draw_pixel_art(canvas, (120, 220), pixel=12, palette=(None, '#E0607E', 'black', 'white'))
draw_pixel_art(canvas, (420, 250), pixel=8)
draw_pixel_art(canvas, (55, 415), pixel=6, file_name='flower.csv', palette=(None, 'black', '#FF0000', 'orange', 'yellow', 'white', '#5ec031'))
draw_pixel_art(canvas, (350, 115), pixel=5, file_name='frank.csv', palette=(None, 'black', '#5ec031', 'white'))
draw_pixel_art(canvas, (315, 380), pixel=15, file_name='frank.csv', palette=(None, 'black', '#5ec031', 'white'))
draw_pixel_art(canvas, (420, 10), pixel=10, palette=(None, '#E0607E', 'black', 'white'))


########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()