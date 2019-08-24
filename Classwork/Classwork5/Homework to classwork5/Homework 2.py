
from tkinter import Canvas, Tk
import random

canvas_width = 800
canvas_height = 400

root = Tk()
root.title("Ball")
c = Canvas(root,width=canvas_width,height=canvas_height,background='pink')
c.pack()


ball_color = 'purple'
ball_width = 60
ball_height = 60
ball_start_x1 = canvas_width/2 - ball_width/2
ball_start_y1 = canvas_height/2 - ball_height/2
ball_start_x2 = canvas_width/2 + ball_width/2
ball_start_y2 = canvas_height/2 + ball_height/2
ball_speed = 15

ball = c.create_oval(ball_start_x1, ball_start_y1, \
                 ball_start_x2, ball_start_y2, \
                 fill = ball_color, width = 0)
dx = 1
dy = 1


def move_left(event):
    (x1,y1,x2,y2) = c.coords(paddle)
    if x1>0:
        c.move(paddle,-20,0)

def move_right(event):
    (x1,y1,x2,y2) = c.coords(paddle)
    if x2 < canvas_width:
        c.move(paddle, 20, 0)
def ball_move():
    global dx, dy
    (bx1,by1,bx2,by2) = c.coords(ball)
    if bx1 <= 0:
        dx = -dx
    if bx2 >= canvas_width:
        dx = -dx
    if by1 <= 0:
        dy = -dy
    if by2 >= canvas_height:
        dy = -dy
    c.move(ball, dx, dy)
    root.after(ball_speed, ball_move) 
c.bind('<Left>',move_left)
c.bind('<Right>',move_right)
c.focus_set()

root.after(ball_speed, ball_move)

root.mainloop()
