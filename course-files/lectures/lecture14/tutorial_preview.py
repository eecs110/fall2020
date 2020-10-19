from tkinter import Tk, Canvas

gui = Tk()
gui.title('Pixel Art')
canvas = Canvas(gui, width=500, height=500, background='#000022')
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################


def make_square(canvas: Canvas, top_left: tuple, width: int, fill_color: str='#84A9C0', outline_color='#DDD'):
    canvas.create_rectangle([
            top_left,  # top_left
            (top_left[0] + width, top_left[1] + width)  # bottom_right
        ],
        fill=fill_color,
        outline=outline_color
    )

frank_pixels = (
    (0, 0, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 2, 2, 2, 2, 2, 0, 0),
    (0, 0, 2, 2, 2, 2, 2, 0, 0),
    (0, 0, 2, 1, 2, 1, 2, 0, 0),
    (0, 0, 2, 2, 2, 2, 2, 0, 0),
    (0, 2, 3, 3, 3, 3, 3, 2, 0),
    (0, 2, 2, 2, 2, 2, 2, 2, 0),
    (0, 2, 2, 2, 2, 2, 2, 2, 0),
    (0, 0, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 2, 2, 0, 2, 2, 0, 0)
)

for row in frank_pixels:
    print(row)




########################## YOUR CODE ABOVE THIS LINE ############################## 
canvas.mainloop()