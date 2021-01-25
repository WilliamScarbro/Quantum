from ipycanvas import Canvas
import numpy as np
import math
from time import sleep

def to_bloch(probabilities,phases,entangled,canvas):
    phases = [p-math.pi/2 for p in phases]
    circle_radius=20
    circle_margin=5
    row_margin = 10
    step = circle_radius*2+circle_margin
    per_row = canvas.width//(step)
    circles_x = []
    circles_y = []
    x_pos = 0
    y_pos = 0
    in_row=0
    for i in range(len(probabilities)):
        circles_x+=[x_pos+circle_radius]
        circles_y+=[y_pos+circle_radius]
        in_row+=1
        if in_row==per_row:
            x_pos=0
            y_pos+=step+row_margin
            in_row=0
        else:
            x_pos+=step
    fill_radii = [circle_radius*prop for prop in probabilities]
    phase_lines_x = [pos+math.cos(phase)*circle_radius for phase,pos in zip(phases,circles_x)]
    phase_lines_y = [pos+math.sin(phase)*circle_radius for phase,pos in zip(phases,circles_y)]
    text_loc_y = [pos+circle_radius+12 for pos in circles_y]
    
    canvas.stroke_circles(circles_x,circles_y,circle_radius)
    canvas.fill_style = "red" if entangled else "green"
    canvas.fill_circles(circles_x,circles_y,fill_radii)
    canvas.stroke_style = "black"
    for i in range(len(circles_x)):
        if probabilities[i]>0.000001:
            canvas.stroke_line(circles_x[i],circles_y[i],phase_lines_x[i],phase_lines_y[i])
    canvas.text_align="center"
    canvas.test_baseline="top"
    canvas.text_font="12px sans-serif"
    canvas.fill_style="black"
    for i in range(len(phases)):
        canvas.fill_text(f"|{i}>",circles_x[i],text_loc_y[i])
        
def print_circles(probabilities,phases,entangled):
    canvas = Canvas(width=300, height=200)
    to_bloch(probabilities,phases,entangled,canvas)
    return canvas

def state_animation(states,wait):
    canvas = Canvas(width=300, height=200)
    display(canvas)
    for state in states:
        canvas.clear()
        to_bloch(*state,canvas)
        sleep(wait)
     