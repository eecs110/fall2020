from tkinter import Canvas, Tk
gui = Tk()
gui.title('Shapes')
canvas = Canvas(gui, width=500, height=300, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
canvas.create_rectangle([
        (0, 100),  # top_left
        (100, 200)  # bottom_right
    ],
    fill='teal'
)
canvas.create_polygon([
        (100, 100),  # coord1
        (200, 100),  # coord2
        (150, 200)
    ], 
    fill='purple'
)
canvas.create_oval([
        (200, 100),  # top_left
        (300, 200)   # bottom_right
    ],  
    fill='hotpink'
)
canvas.create_polygon([
        (300, 100),  # coord1
        (400, 100),  # coord2
        (350, 200)
    ], 
    fill='purple'
)
canvas.create_rectangle([
        (400, 100),  # top_left
        (500, 200)  # bottom_right
    ],
    fill='teal'
)




########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()