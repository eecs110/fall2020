
'''
This demo shows you how you can create a new image by clicking the screen.
'''
from tkinter import Canvas, Tk
import utilities
import keycodes

gui = Tk()
gui.title('Keyboard Event Handler')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################
KEY_PRESS = '<Key>'

def move_circle(event):
    distance = 10
    if event.keycode == keycodes.get_up_keycode():
        utilities.update_position_by_tag(canvas, tag='circle', x=0, y=-distance)
    elif event.keycode == keycodes.get_down_keycode():
        utilities.update_position_by_tag(canvas, tag='circle', x=0, y=distance)
    elif event.keycode == keycodes.get_left_keycode():
        utilities.update_position_by_tag(canvas, tag='circle', x=-distance, y=0)
    elif event.keycode == keycodes.get_right_keycode():
        utilities.update_position_by_tag(canvas, tag='circle', x=distance, y=0)
    else:
        print('Keycode:', event.keycode, 'not handled by this if/elif/else statement.')

canvas.bind(KEY_PRESS, move_circle)
canvas.focus_set()
utilities.make_circle(canvas, (window_width/2, window_height/2), 50, color='hotpink', tag='circle')

########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()