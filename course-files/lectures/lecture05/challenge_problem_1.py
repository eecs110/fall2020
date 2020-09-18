from tkinter import Canvas, Tk

#####################################
# begin make_grid function definition
#####################################
def make_grid(canvas, w, h):
    interval = 100

    # Delete old grid if it exists:
    canvas.delete('grid_line')
    # Creates all vertical lines at intevals of 100
    for i in range(0, w, interval):
        canvas.create_line(i, 0, i, h, tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, interval):
        canvas.create_line(0, i, w, i, tag='grid_line')

    # Creates axis labels
    offset = 2
    for y in range(0, h, interval):
        for x in range(0, w, interval):
            canvas.create_oval(
                x - offset, 
                y - offset, 
                x + offset,  
                y + offset, 
                fill='black'
            )
            canvas.create_text(
                x + offset, 
                y + offset, 
                text="({0}, {1})".format(x, y),
                anchor="nw", 
                font=("Purisa", 8)
            )
###################################
# end make_grid function definition
###################################


'''
1. Write a program that prompts the user for a color, which can be any string representation of a color
2. Then, draw a rectangle (of any dimensions) with that color
'''

user_color = input('Hey, what color do you want this rectangle to be? ')
# print(user_color)


# initialize window
window = Tk()
canvas = Canvas(window, width=700, height=350, background='white')
canvas.pack()

canvas.create_rectangle(
    [ (100, 25), (250, 75) ],  #  coords: top-left, bottom-right
    fill=user_color)

make_grid(canvas, 700, 350)

canvas.mainloop()





