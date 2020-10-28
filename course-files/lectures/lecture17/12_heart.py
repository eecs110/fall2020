import utilities

canvas = utilities.create_canvas_window()
##################################################################################
# Your code below this line...


# Your job: Figure out how to use the data in the heart
# file to draw a heart

f = open(utilities.get_file_path('heart.csv'))
for line in f.readlines():
    print(line)

# palette = ['white', '#E0607E', 'black', 'white']
# utilities.make_square(canvas, (100, 100), 20, color=palette[1])

# Your code above this line
##################################################################################
canvas.mainloop()