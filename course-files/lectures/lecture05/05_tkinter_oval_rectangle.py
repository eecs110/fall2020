from tkinter import Canvas, Tk

# initialize window
gui = Tk()
canvas = Canvas(gui, width=700, height=350, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
# help(canvas.create_oval)

# Documentation: https://effbot.org/tkinterbook/canvas.htm#Tkinter.Canvas.create_oval-method
'''
some optional parameters: 
activefill= Fill color to use when the mouse pointer is moved over the item
fill= Fill color. An empty string means transparent.
activeoutline=Active outline color
outline=Outline color. Default is “black”.
width=Outline width
tags=A tag to attach to this item, or a tuple containing multiple tags.
'''
canvas.create_oval([ (50, 150), (150, 250) ], # top left x-y, bottom right x-y
    fill='#FF4136',
    width=5,
    activefill='hotpink',
    activeoutline='#999999'
)

# Documentation: https://effbot.org/tkinterbook/canvas.htm#Tkinter.Canvas.create_rectangle-method
canvas.create_rectangle(
    [ (500, 25), (650, 75) ],  #  coords: top-left, bottom-right
    fill="#3D9970")

########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()