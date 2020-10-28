import utilities

canvas = utilities.create_canvas_window()
##################################################################################
# Your code below this line...


# Your job: Figure out how to use the data in the heart
# file to draw a heart


# start at top_left position (100, 100)
x = 100
y = 100
pixel = 20
palette = ['white', '#E0607E', 'black', 'white']

f = open(utilities.get_file_path('heart.csv'))
for line in f.readlines():
    cells = line.split(',')
    x = 100 # reset x-position to 100 (start of every row)
    for cell in cells:
        cell = int(cell)
        fill_color = palette[cell]
        utilities.make_square(canvas, (x, y), pixel, 
            color=fill_color, stroke_width=1
        )
        x += pixel
    y += pixel # go down to next row


# Your code above this line
##################################################################################
canvas.mainloop()