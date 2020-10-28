from tkinter import Canvas, Tk

gui = Tk()
gui.title('Intro')
canvas = Canvas(gui, width=300, height=300, background='white')
canvas.pack()

def make_circle(canvas, center, radius, color='white'):
    x, y = center
    return canvas.create_oval(
        [ x - radius, y - radius, x + radius, y + radius ],
        fill=color
    )

##################### Your Code Here ###########################

user_data = input('Where should we draw your circle (input as x,y,radius,color)? ')  # 123,55,7,hotpink
print(user_data)


## What do we do now?
#  1. We need to convert user_data into a form that can be used by the circle function
#  2. We need to invoke the make_circle function with the correct arguments and
#     data types



##################### Your Code Here ###########################
canvas.mainloop()