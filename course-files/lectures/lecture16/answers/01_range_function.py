from tkinter import Canvas, Tk
import random
import time
import utilities

gui = Tk()
gui.title('Circle')
canvas = Canvas(gui, width=500, height=500)
canvas.pack()

def make_rect(canvas, center, radius, color='white', tag=None, stroke_width=1, outline=None):
    x, y = center
    canvas.create_rectangle(
        [ x - radius, y - radius, x + radius, y + radius ],
        fill=color,
        width=stroke_width,
        tags=tag,
        outline=outline
    )
########################## YOUR CODE BELOW THIS LINE ##############################

palette = ['#f0a202', '#f18805', '#d95d39', '#0e1428', '#7b9e89']


# first: create all of the squares:
for i in range(0, 100):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    radius = random.randint(1, 30)
    fill = random.choice(palette)
    tag_name = 'sq_' + str(i) # give each square a unique tag
    make_rect(canvas, (x, y), radius, color=fill, tag=tag_name)
    gui.update()
    time.sleep(0.001)

tags_of_squares_i_want_to_animate = [
    'sq_97', 'sq_98', 'sq_99'
]
# if you later want to animate anything:
while True:
    for tag in tags_of_squares_i_want_to_animate:
        utilities.update_position_by_tag(canvas, tag, x=0, y=2)
    gui.update()
    time.sleep(0.001)



########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()