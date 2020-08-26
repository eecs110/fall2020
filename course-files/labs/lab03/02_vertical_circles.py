from tkinter import Canvas, Tk
from helpers import make_circle

gui = Tk()
gui.title('Circle')
canvas = Canvas(gui, width=500, height=500, background='#000022')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################



# Challenge 1: 
#   How could I rewrite the following code using a while loop?

make_circle(canvas, (100, 50), 25)
make_circle(canvas, (100, 100), 25)
make_circle(canvas, (100, 150), 25)
make_circle(canvas, (100, 200), 25)
make_circle(canvas, (100, 250), 25)
make_circle(canvas, (100, 300), 25)



########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()