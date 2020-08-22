from tkinter import Canvas, Tk


def make_circle(canvas, center, radius, color='white', tag=None, stroke_width=1, outline=None):
    x, y = center
    return canvas.create_oval(
        [ x - radius, y - radius, x + radius, y + radius ],
        fill=color,
        width=stroke_width,
        tags=tag,
        outline=outline
    )

def get_file_path(file_name):
    import os
    import sys
    dir_path = os.path.dirname(sys.argv[0])
    return os.path.join(dir_path, file_name)

def create_canvas_window(window_width=None, window_height=None, title='My Window', bg_color='white'):
    gui = Tk()
    gui.title(title)
    window_width = window_width or gui.winfo_screenwidth()
    window_height = window_height or gui.winfo_screenheight()
    canvas = Canvas(gui, width=window_width, height=window_height, background=bg_color)
    canvas.pack()
    return canvas