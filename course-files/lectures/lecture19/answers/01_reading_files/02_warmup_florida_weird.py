import utilities
from tkinter import Canvas, Tk
import time

gui = Tk()
gui.title('Florida')
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='white')
canvas.pack()
##################################################################################
point_list = []
f = open(utilities.get_file_path('florida.csv'))
for line in f.readlines():
    line = line.replace('\n', '')
    items = line.split(',')
    x = float(items[0])
    y = float(items[1])
    point_list.append((x, y))

canvas.create_polygon(point_list, fill='white', outline='black', tag='florida')
gui.update()

while True:
    center = utilities.get_center(canvas, 'florida')
    width = utilities.get_width(canvas, 'florida')
    print(center, width)
    shape_ids = canvas.find_withtag('florida')
    for shape_id in shape_ids:
        flipped_coordinates = []
        shape_coords = canvas.coords(shape_id)
        counter = 0
        for num in shape_coords:
            if counter % 2 == 0:
                shape_coords[counter] = -num + center[0] + width/2
            counter += 1
            canvas.coords(shape_id, shape_coords)
            gui.update()
            time.sleep(0.01)
    time.sleep(2)

# Your code above this line
##################################################################################
canvas.mainloop()