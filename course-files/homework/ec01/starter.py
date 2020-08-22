from tkinter import Canvas, Tk, Scale, DoubleVar, CENTER
import helpers
import utilities
import helpers
import time
import random
import math

gui = Tk()
gui.title('Covid19 Simulation')

# initialize canvas:
window_width = 1000
window_height = 600
canvas = Canvas(gui, width=1000, height=600, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# epidemiology info 
person_count = 300 # how many people are in the simulation
infection_rate = 0.9 # how likely it is for a person to catch it provided he or she is within the infection radius
infection_radius = 50 # see above
removal_time =2 # time it takes for a person to either recover or die or be isolated
social_activity= 10# how fast the persons travel
max_speed = social_activity

# set up visual info
person_size = 5
healthy_colour = '#00f708'
infected_colour = '#e81313'
removed_colour = '#3c5980'

# the list will contain all the persons being simulated
# in particular, each list item/element will be another list 
# containing the person's location, speed and 
# whether the person is healthy, infected, or removed,
# and how many days since infection

person_list =[] 
counter = 0

xloc = random.uniform(0, window_width)
yloc = random.uniform(0, window_height)
days = 0
person_list.append([xloc,yloc,0,0, 'infected', days])
utilities.make_circle(canvas, (xloc,yloc), radius=person_size,color=infected_colour, tag="person"+str(counter))
counter += 1



########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()