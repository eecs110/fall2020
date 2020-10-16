from tkinter import Canvas, Tk
import time
import shapes

gui = Tk()
gui.title('Animation')
canvas = Canvas(gui, width=500, height=500, background='white')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# Challenge:
# 1. Turn the car code into a function, with a customizable 
#    position, color, and tag (let’s skip size for now b/c the arithmetic 
#    is a little tedious and you’re doing that in your homework).
# 2. Note that the “tag” parameter is useful so that you can refer to 
#    the car later when you want to animate it.
# 3. Create 3 cars (different tags, sizes, and colors)
# 4. Animate each car differently


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