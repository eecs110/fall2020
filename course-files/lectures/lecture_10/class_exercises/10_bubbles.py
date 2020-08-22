import utilities

canvas = utilities.create_canvas_window()
##################################################################################
# Your code below this line...


# Your job: Modify the code below so that as
# you loop through each line of the file, you:
# 1. create a variable called "center" that 
#    stores the first and second number in the line
#    as a (tuple of ints). 
# 2. Create a variable called "radius" that stores the
#    third number in the line.
# 3. Passes the center and radius variables into the
#    utilities.make_circle function as arguments.



f = open(utilities.get_file_path('bubbles.csv'))
for line in f.readlines():
    data = line.split(',')
    # how do we extract the x, y, and radius?
    x = int(data[0])
    y = int(data[1])
    radius = int(data[2])
    # print(x, y, radius)
    # # goal: (x, y), radius
    utilities.make_circle(canvas, (x, y), radius)


# Your code above this line
##################################################################################
canvas.mainloop()