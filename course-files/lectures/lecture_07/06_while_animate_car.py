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


#make car:
top_id = shapes.make_rectangle(canvas, (100, 20), 100, 40, tag='car_1')
bottom_id = shapes.make_rectangle(canvas, (50, 50), 200, 45, tag='car_1')
wheel1_id = shapes.make_circle(canvas, (100, 100), 20, color='black', tag='car_1')
wheel2_id = shapes.make_circle(canvas, (200, 100), 20, color='black', tag='car_1')


# move car:
shapes.move(canvas, 'car_1', x=60, y=0)
gui.update()
time.sleep(1)

# move car again:
shapes.move(canvas, 'car_1', x=60, y=0)
gui.update()
time.sleep(1)

# move car again:
shapes.move(canvas, 'car_1', x=60, y=0)
gui.update()
time.sleep(1)







########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()