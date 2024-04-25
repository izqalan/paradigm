'''
Created on April 2024

@author:
Lam Wei Long(A189310)
Izqalan Nor'Izad (A189289)
Nuruddin Naim Bin Abu Hanifah(A186277)
'''

import turtle 

# this will create an empty window canvas for our digital aquarium lol
canvaWindow = turtle.Screen()

# Hello team, please add documentation like this
# So that we can understand what the function does
# and how to use it
# - @izqalan

# Triangle function
# Parameters: t - turtle object
#             x,y - starting position of the triangle
#             size - size of the triangle
#             colorP - pen color
#             colorF - fill color
#             point - left, right, or up. default is down
# Return: None
def drawTriangle(t,x,y,size,colorP="black",colorF="white", point="up"):
    t.pencolor(colorP) 
    t.fillcolor(colorF)
    # Lift the pen up - no drawing when moving
    t.up()
    t.begin_fill() # Start filling in the shape
    
    point = point.lower()

    if point == "down":
        # go to point edge, y-size because we want to draw from the bottom
        t.goto(x, y-size)
        t.down()
        # draw to right up edge, hence the x+size (right) and y+size (up)
        t.goto(x+size, y+size)
        # draw to left (x-size) edge and maintain current y position as before (y+size)
        t.goto(x-size, y+size)
        # draw back to the starting point
        t.goto(x, y-size)
    elif point == "left":
        # go left from the starting point x
        t.goto(x-size, y)
        t.down()
        # draw to the right x+ and up edge y+
        t.goto(x+size, y+size)
        # go down (y-) and maintain x plane
        t.goto(x+size, y-size)
        # go back to starting point. left x- and up y plane
        t.goto(x-size, y)
    elif point == "right":
        # uhhh, basically just an inverse of left
        t.goto(x+size, y)
        t.down()
        t.goto(x-size, y+size)
        t.goto(x-size, y-size)
        t.goto(x+size, y)
    else:
        # default is up
        # this is basically the same as down but in reverse
        t.goto(x, y+size)
        t.down()
        t.goto(x+size, y-size)
        t.goto(x-size, y-size)
        t.goto(x, y+size)
    
    t.up()
    t.end_fill() # End filling in the shape

# Circle function
# Parameters: t - turtle object
#             x,y - starting position of the circle
#             r - radius of the circle
#             colorP - pen color
#             colorF - fill color
# Return: None
def drawCircle(t,x,y,r,colorP="black",colorF="white"):
    # This is pretty self explanatory
    # Do I have to explain this?
    # I mean, it's a circle
    # only thing this function does is set the coordinates
    t.pencolor(colorP)
    t.fillcolor(colorF)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    # There's a circle function in turtle
    t.circle(r)
    t.end_fill()

def drawRectangle(t,x,y,w,h,colorP="black",colorF="white"):
    t.pencolor(colorP)
    t.fillcolor(colorF)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.goto(x+w,y)
    t.goto(x+w,y+h)
    t.goto(x,y+h)
    t.goto(x,y)
    t.end_fill()
                                                                                       
def mainDraw():
    canvaWindow.colormode(255) 
    canvaWindow.bgcolor(17,178,255)      # fill color
    
    draw_pen = turtle.Turtle()    # you can rename the turtle if you want
    
    # drawRectangle(draw_pen,-200,-300,500,500,"black","blue")
    # drawRectangle(draw_pen,0,0,300,300,"yellow","red")
    # drawTriangle(draw_pen,0,0,100,"black","blue",0)
    # drawTriangle(draw_pen,0,100,75,"black","red", "down")
    # drawTriangle(draw_pen,0,0,10,"black","blue")
    # drawTriangle(draw_pen,0,-100,50,"black","red", "left")
    # drawTriangle(draw_pen,0,-200,50,"black","red", "right")
    # drawTriangle(draw_pen,0,100,100,"black","red", "left")
    drawCircle(draw_pen,0,300,20,"black","red")


if __name__ == '__main__':
    mainDraw()



canvaWindow.exitonclick()
