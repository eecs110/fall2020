from tkinter import Canvas, Tk
import time
import shapes

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################


#make car:
top_id = shapes.make_rectangle(canvas, (100, 20), 100, 40, tag='car_1')
bottom_id = shapes.make_rectangle(canvas, (50, 50), 200, 45, tag='car_1')
wheel1_id = shapes.make_circle(canvas, (100, 100), 20, color='black', tag='car_1')
wheel2_id = shapes.make_circle(canvas, (200, 100), 20, color='black', tag='car_1')


while True:
    # move car:
    shapes.move(canvas, 'car_1', x=3, y=0)
    gui.update()
    time.sleep(.001)







########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()