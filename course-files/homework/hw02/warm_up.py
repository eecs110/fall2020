from tkinter import Canvas, Tk
import helpers

# initialize window
gui = Tk()
canvas = Canvas(gui, width=700, height=350, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# make a label:
canvas.create_text(
    (210, 210), 
    text="Hello world!", 
    font=("Purisa", 32),
    anchor='nw'  # align to "northwest" corner
)

# make an oval:
canvas.create_oval(
    [ (50, 150),  (150, 250) ], # top left x-y, bottom right x-y
    fill='#FF4136',
    width=5
)

# make a polygon
canvas.create_polygon(
    [ (370, 150),  (630, 150), (500, 350) ],  # list of x-y pairs
    width=2,
    fill='#BCD39C',
    smooth=True)  #make smooth false for angular polygon

# make a line:
canvas.create_line(
    [ (10, 0),  (210, 100),  (420, 0),  (630, 100) ],  # list of x-y pairs
    width=3)

# make an arc:
canvas.create_line(
    [ (350, 50),  (430, 50),  (450, 200) ],  # list of x-y pairs
    width=5,
    fill='#0074D9',
    splinesteps=15,
    smooth=True)

# make line that looks like an arc:
canvas.create_arc(
        [
            (150, 50), 
            (350, 350)
        ],
        width=5,
        style='arc',
        outline='#0074D9'
    )

# make a dashed line: 
canvas.create_line(
    [ (10, 100),  (210, 0),  (420, 100),  (630, 10) ], 
    fill="#3D9970", 
    dash=(4, 4), 
    width=3)

# make a curvy line:
canvas.create_line(
    [
        (0,   100), 
        (50,  150), 
        (100, 100), 
        (150, 150), 
        (200, 100), 
        (250, 150), 
        (300, 100), 
        (350, 150), 
        (400, 100)
    ], 
    splinesteps=20,
    width=3, 
    smooth=True)

# make a rectangle
canvas.create_rectangle(
    [ (500, 25), (650, 75) ],  #  coords: top-left, bottom-right
    fill="#3D9970")

helpers.make_grid(canvas, 700, 350)

########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()