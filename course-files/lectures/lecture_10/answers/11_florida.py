import utilities

canvas = utilities.create_canvas_window()
##################################################################################
# Your code below this line...

point_list = []
f = open(utilities.get_file_path('florida.csv'))
for line in f.readlines():
    line = line.replace('\n', '')
    items = line.split(',')
    x = float(items[0])
    y = float(items[1])
    point_list.append((x, y))

canvas.create_polygon(point_list, fill='#e28894')


# Your code above this line
##################################################################################
canvas.mainloop()