import utilities

canvas = utilities.create_canvas_window()

##################################################################################
# Your code below this line...

f = open(utilities.get_file_path('bubbles.csv'))
for line in f.readlines():
    line = line.replace('\n', '')
    items = line.split(',')
    x = int(items[0])
    y = int(items[1])
    radius = int(items[2])
    # print([x, y, radius])
    utilities.make_circle(canvas, (x, y), radius)

# Your code above this line
##################################################################################
canvas.mainloop()