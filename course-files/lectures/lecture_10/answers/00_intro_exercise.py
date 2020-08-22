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
tokens = user_data.split(',')
print(tokens)
x = int(tokens[0])
y = int(tokens[1])
r = int(tokens[2])
fill = tokens[3]
make_circle(canvas, (x, y), r, color=fill)

# Challenge: How would you keep prompting the user for a circle?

##################### Your Code Here ###########################
canvas.mainloop()