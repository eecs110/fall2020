from tkinter import Canvas, Tk
import time
import shapes

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# make circle
shapes.make_circle(canvas, (100, 100), 40, color='hotpink', tag='circle_1')
shapes.make_circle(canvas, (100, 100), 20, color='teal', tag='circle_2')

while True:
    shapes.move(canvas, 'circle_1', x=2, y=0)
    shapes.move(canvas, 'circle_2', x=0, y=3)
    gui.update()
    time.sleep(.001)







########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()