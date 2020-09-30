from tkinter import Canvas, Tk

# initialize window
gui = Tk()
canvas = Canvas(gui, width=700, height=450, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

canvas.create_polygon(
    [ 
        (300, 100), # top-most coordinate
        (400, 200), # right-most coordinate
        (300, 300), # bottom-most coordinate
        (200, 200)  # left-most coordinate
    ],
    fill='teal',
    width=5,
    outline='black',
    activefill='hotpink',
    activeoutline='#999999'
)


########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()