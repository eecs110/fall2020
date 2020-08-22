import utilities
from tkinter import Canvas, Tk
import time

gui = Tk()
gui.title('Bubbles from file')
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
    time.sleep(2)
    utilities.flip(canvas, 'florida')
    gui.update()

# Your code above this line
##################################################################################
canvas.mainloop()