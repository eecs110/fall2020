from tkinter import Canvas

def make_circle(canvas:Canvas, center:tuple, radius:int, color:str='#FF4136', tag:str=None, stroke_width:int=1, outline:str=None):
    x, y = center
    canvas.create_oval(
        [ x - radius, y - radius, x + radius, y + radius ],
        fill=color,
        width=stroke_width,
        tags=tag,
        outline=outline
    )