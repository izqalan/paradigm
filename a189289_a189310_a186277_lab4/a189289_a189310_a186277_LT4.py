'''
Created on April 2024

@author:
Lam Wei Long(A189310)
Izqalan Nor'Izad (A189289)
Nuruddin Naim Bin Abu Hanifah(A186277)
'''
import turtle
import random

#this 4 line is like initialization
canvaWindow = turtle.Screen()       # this will create an empty window canvas for our digital aquarium
canvaWindow.setup(width=1024, height=576) #just force set, but maximize can change size
canvaWindow.colormode(255)          # enable to use RGB mode of color fill
canvaWindow.bgcolor(17,178,255)     # fill color
draw_pen = turtle.Turtle()          # you can rename the turtle if you want
draw_pen.penup()

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

def draw_fish(x, y, color, direction="left"):
    draw_pen.penup()
    draw_pen.goto(x, y)
    draw_pen.pendown()
    draw_pen.color(color)
    draw_pen.begin_fill()
    if direction == "left":
        # Draw body (big diamond shape)
        draw_pen.goto(x - 60, y + 30)
        draw_pen.goto(x, y + 60)
        draw_pen.goto(x + 60, y + 30)
        draw_pen.goto(x, y)
        # Draw tail (small triangle)
        draw_pen.goto(x + 60, y + 30)
        draw_pen.goto(x + 80, y + 10)
        draw_pen.goto(x + 80, y + 50)
        draw_pen.goto(x + 60, y + 30)
    elif direction == "right":
        # Draw body (big diamond shape)
        draw_pen.goto(x + 60, y + 30)
        draw_pen.goto(x, y + 60)
        draw_pen.goto(x - 60, y + 30)
        draw_pen.goto(x, y)
        # Draw tail (small triangle)
        draw_pen.goto(x - 60, y + 30)
        draw_pen.goto(x - 80, y + 10)
        draw_pen.goto(x - 80, y + 50)
        draw_pen.goto(x - 60, y + 30)
    draw_pen.end_fill()
    # Draw eye
    draw_pen.penup()
    if direction == "left":
        draw_pen.goto(x - 30, y + 25)
    elif direction == "right":
        draw_pen.goto(x + 30, y + 25)
    draw_pen.pendown()
    draw_pen.color("black")
    draw_pen.begin_fill()
    draw_pen.circle(5)
    draw_pen.end_fill()
    draw_pen.penup()

def draw_starfish(x, y, size, color):
    draw_pen.penup()
    draw_pen.goto(x, y)
    draw_pen.pendown()
    draw_pen.color(color)
    draw_pen.begin_fill()
    for _ in range(5):
        draw_pen.forward(size)
        draw_pen.right(144)
        draw_pen.forward(size)  # Move forward again to create the inner part of the arm
        draw_pen.left(72)
    draw_pen.end_fill()
    draw_pen.penup()

def draw_rock_hexagon(x, y, size, color):
    draw_pen.penup()
    draw_pen.goto(x, y)
    draw_pen.pendown()
    draw_pen.color(color)
    draw_pen.begin_fill()
    draw_pen.setheading(random.randint(50, 360))#make it look like rotate instead of fixed angle
    for _ in range(6):
        #draw_pen.forward(size + random.randint(-10, 10))
        draw_pen.forward(size)
        draw_pen.right(60)
    draw_pen.end_fill()
    draw_pen.penup()

def draw_rock_octagon(x, y, size, color):
    draw_pen.penup()
    draw_pen.goto(x, y)
    draw_pen.pendown()
    draw_pen.color(color)
    draw_pen.begin_fill()
    draw_pen.setheading(random.randint(50, 360))#make it look like rotate instead of fixed angle
    for _ in range(8):
        #draw_pen.forward(size + random.randint(-10, 10))
        draw_pen.forward(size)
        draw_pen.right(45)
    draw_pen.end_fill()
    draw_pen.penup()

def draw_round_fish(x, y, size, color):

    # draw_pen.speed("fastest")  # Increase drawing speed
    draw_pen.penup()
    draw_pen.goto(x, y)
    draw_pen.pendown()
    draw_pen.color(color)
    draw_pen.begin_fill()
    # Draw the round fish shape
    draw_pen.left(45)
    draw_pen.forward(size)
    draw_pen.right(135)
    draw_pen.forward(size + 5)
    draw_pen.right(130)
    draw_pen.forward(size - 12)
    draw_pen.left(90)
    draw_pen.right(90)
    draw_pen.circle(size, 90) #Make a round upper body of the fish
    draw_pen.left(90)
    draw_pen.circle(size, 90) #Make a round lower body of the fish
    draw_pen.end_fill()

  # Draw the eye
    draw_pen.penup()
    draw_pen.left(130)
    draw_pen.forward(size)
    draw_pen.pendown()
    draw_pen.color("black")
    draw_pen.begin_fill()
    draw_pen.circle(5)
    draw_pen.end_fill()
    draw_pen.penup()

                                                            
def mainDraw():
       
    # drawRectangle(draw_pen,-200,-300,500,500,"black","blue")
    # drawRectangle(draw_pen,0,0,300,300,"yellow","red")
    # drawTriangle(draw_pen,0,0,100,"black","blue",0)
    # drawTriangle(draw_pen,0,100,75,"black","red", "down")
    # drawTriangle(draw_pen,0,0,10,"black","blue")
    # drawTriangle(draw_pen,0,-100,50,"black","red", "left")
    # drawTriangle(draw_pen,0,-200,50,"black","red", "right")
    # drawTriangle(draw_pen,0,100,100,"black","red", "left")
    # drawCircle(draw_pen,0,300,20,"black","red")


    draw_round_fish(100, 200, 50, 'orange')    
    draw_round_fish(-100, 150, 50, 'orange')   

    for _ in range(5):
         draw_rock_hexagon(random.randint(-400, 400), -250, 80, "#7B2E0D")
    for _ in range(5):
         draw_rock_octagon(random.randint(-400, 400), -250, 80, "#98411B")

    draw_rock_hexagon(-250, -250, 80, "gray")
    draw_rock_hexagon(-300, -250, 80, "#A9512B")
    draw_rock_hexagon(150, -250, 80, "#BD430F")
    draw_rock_octagon(-150, -250, 80, "#A44116")
    draw_rock_octagon(50, -250, 80, "#47371C")
    draw_fish(150, 50, "red")                           # Draw the fish facing left
    draw_fish(-200, -50, "blue", direction="right")     # Draw the fish facing right
    draw_starfish(-200,-200, 30, "#FF9B57") 
    

if __name__ == '__main__':
    mainDraw()


draw_pen.hideturtle() #make the turtle invisible, so we can view the aquarium
canvaWindow.exitonclick() 
