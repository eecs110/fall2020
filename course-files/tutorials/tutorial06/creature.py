from tkinter import Canvas
import utilities

def make_creature(canvas, center, size=100, tag='creature', fill='lightgray'):
    radius = size / 2
    # just a demo of how you might think about making your creature:
    left_eye_pos = (center[0] - radius / 4, center[1] - radius / 5)
    right_eye_pos = (center[0] + radius / 4, center[1] - radius / 5)
    eye_width = eye_height = radius / 10

    # IMPORTANT that I'm tagging each of the shapes that makes up my "make_creature"
    # with the tag that the user passed in:
    utilities.make_circle(canvas, center, radius, color=fill, tag=tag)
    utilities.make_oval(canvas, left_eye_pos, eye_width, eye_height, color='black', tag=tag)
    utilities.make_oval(canvas, right_eye_pos, eye_width, eye_height, color='black', tag=tag)
    utilities.make_line(canvas, [
        (center[0] - radius / 2, center[1] + radius / 3), 
        (center[0], center[1] + radius / 1.2), 
        (center[0] + radius / 2, center[1] + radius / 3)
    ], curvy=True, tag=tag)