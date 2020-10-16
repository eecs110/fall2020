from tkinter import Canvas, Tk
import time
import shapes

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

def make_car(canvas:Canvas, top_left:tuple=(0, 0), color:str="#3D9970", tag:str=None):
    x, y = top_left
    shapes.make_rectangle(canvas, (x + 50, y), 100, 40, color=color, tag=tag)
    shapes.make_rectangle(canvas, (x, y + 30), 200, 45, color=color, tag=tag)
    shapes.make_circle(canvas, (x + 50, y + 80), 20, color='black', tag=tag)
    shapes.make_circle(canvas, (x + 150, y + 80), 20, color='black', tag=tag)

make_car(canvas, (100, 100), tag='car_1')
make_car(canvas, (-100, 250), tag='car_2', color='yellow')
make_car(canvas, (500, 400), tag='car_3', color='hotpink')

while True:
    # move car:
    shapes.move(canvas, 'car_1', x=3, y=0)
    shapes.move(canvas, 'car_2', x=10, y=0)
    shapes.move(canvas, 'car_3', x=-4, y=0)
    gui.update()
    time.sleep(.001)



########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()