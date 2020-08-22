from tkinter import Canvas, Tk
import time
import shapes

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# Challenge:
# Do the same thing as in 05_while_animate, but with
# all 4 shapes: 
#   1. Make the car smoothly drive across the screen
#   2. Make it drive backwards (on your own)
#   3. Make it drive vertically (on your own)
#   4. Make it drive diagonally (on your own)
#   5. If it gets to the end, of the screen, 
#      make it reverse directions (on your own)
#   6. Make it accelerate (on your own)



def make_car(canvas:Canvas, top_left:tuple, color='hotpink', tag='car'):
    x = top_left[0]
    y = top_left[1]
    #make car:
    top_id = shapes.make_rectangle(canvas, (x + 50, y-30), 100, 40, color=color, tag=tag)
    bottom_id = shapes.make_rectangle(canvas, (x, y), 200, 45, color=color, tag=tag)
    wheel1_id = shapes.make_circle(canvas, (x + 50, y + 50), 20, color='black', tag=tag)
    wheel2_id = shapes.make_circle(canvas, (x + 150, y + 50), 20, color='black', tag=tag)

make_car(canvas, (100, 100), tag='car_1')
make_car(canvas, (150, 300), color='teal', tag='car_2')
make_car(canvas, (200, 0), color='blue', tag='car_3')

while True:
    # move car:
    shapes.move(canvas, 'car_1', x=6, y=0)
    shapes.move(canvas, 'car_3', x=0, y=5)
    
    gui.update()
    time.sleep(.1)







########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()
