def make_circle(canvas, center, radius, color='#FF4136', tag=None):
    x, y = center
    return canvas.create_oval(
        [ x - radius, y - radius, x + radius, y + radius ],
        fill=color,
        width=1,
        tag=tag
    )

def make_rectangle(canvas, top_left, width, height, color="#3D9970", tag=None):
    x, y = top_left
    # print(x, y, x, y, x + width, y + height)
    return canvas.create_rectangle(
        x, y, x + width, y + height, 
        fill=color, 
        width=0,
        tag=tag
    )

def get_coordinates(canvas, id):
    # returns (x1, y1, x2, y2)
    return canvas.coords(id)

def get_top(canvas, id):
    return canvas.coords(id)

def move(canvas, tag, x, y):
    ids = canvas.find_withtag(tag)
    for id in ids:
        canvas.move(id, x, y)