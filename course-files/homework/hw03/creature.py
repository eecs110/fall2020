import helpers

def make_creature(canvas):
    # face: 
    helpers.make_circle(canvas, (250, 150), 100, fill='teal')
    
    # left eye: 
    helpers.make_oval(canvas, (225, 130), 10, 18, fill='black')
    
    # right eye:
    helpers.make_oval(canvas, (275, 130), 10, 18, fill='black')