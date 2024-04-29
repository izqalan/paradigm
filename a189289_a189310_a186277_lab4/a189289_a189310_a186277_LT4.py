'''
Created on April 2024

@author:
Lam Wei Long(A189310)
Izqalan Nor'Izad (A189289)
Nuruddin Naim Bin Abu Hanifah(A186277)
'''
import turtle
import random
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

def draw_fish(draw_pen,x, y, color, direction="left"):
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

def draw_starfish(draw_pen,x, y, size, color):
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

def draw_rock_hexagon(draw_pen,x, y, size, color):
    draw_pen.penup()
    draw_pen.goto(x, y)
    draw_pen.pendown()
    draw_pen.color(color)
    draw_pen.begin_fill()
    draw_pen.setheading(random.randint(0, 180))#make it look like rotate instead of fixed angle
    for _ in range(6):
        #draw_pen.forward(size + random.randint(-10, 10))
        draw_pen.forward(size)
        draw_pen.right(60)
    draw_pen.end_fill()
    draw_pen.penup()

def draw_rock_octagon(draw_pen,x, y, size, color):
    draw_pen.penup()
    draw_pen.goto(x, y)
    draw_pen.pendown()
    draw_pen.color(color)
    draw_pen.begin_fill()
    draw_pen.setheading(random.randint(0, 180))#make it look like rotate instead of fixed angle
    for _ in range(8):
        #draw_pen.forward(size + random.randint(-10, 10))
        draw_pen.forward(size)
        draw_pen.right(45)
    draw_pen.end_fill()
    draw_pen.penup()

def draw_round_fish(draw_pen,x, y, size, color):

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

def draw_seaweed(draw_pen,x, y, size, color):
    draw_pen.penup()
    draw_pen.goto(x, y)
    draw_pen.pendown()
    draw_pen.color(color)
    draw_pen.begin_fill()
    # draw the seaweed
    # move up to size
    # each leave have to increment by +10
    # because each leave is 10 pixel higher than the previous one
    draw_pen.goto(x, y + size)
    # draw to leaves to the right and increase the size/height by +10
    draw_pen.goto(x + 10, y + size + 10)
    # draw to leaves to the left and increase the size/height by +20
    draw_pen.goto(x - 10, y + size + 20)
    # draw to leaves to the right and increase the size/height by +30
    draw_pen.goto(x + 10, y + size + 30)
    draw_pen.goto(x - 10, y + size + 40)
    draw_pen.goto(x, y + size + 50)
    draw_pen.end_fill()
    draw_pen.penup()

def draw_octupus(draw_pen,x, y, size, color):
    # Draw the octopus body
    draw_pen.penup()
    draw_pen.goto(x, y)
    draw_pen.pendown()
    draw_pen.color(color)
    draw_pen.begin_fill()
    draw_pen.circle(size)

    # Draw the octopus legs 
    for _ in range(8):
        draw_pen.penup()
        draw_pen.goto(x,y)
        draw_pen.pendown()
        draw_pen.forward(40) # move the legs foward to 40 
        draw_pen.backward(40) # move the legs backward to 40 
        draw_pen.left(45) # change the direction of turtle by 45 degree to the left

    draw_pen.end_fill()
    draw_pen.penup()

  # Draw the eye
    draw_pen.penup()
    draw_pen.left(120)
    draw_pen.forward(size)
    draw_pen.pendown()
    draw_pen.color("black")
    draw_pen.begin_fill()
    draw_pen.circle(5)
    draw_pen.end_fill()
    draw_pen.penup()


def draw_bubble(draw_pen,x, y, size, color):

    draw_pen.speed("fastest")  # Increase drawing speed
    draw_pen.penup()
    draw_pen.goto(x, y)
    draw_pen.pendown()
    draw_pen.color(color)
    draw_pen.begin_fill()
    draw_pen.circle(size)
    draw_pen.end_fill() #Draw a circle based on random input
    draw_pen.penup()
             
def mainDraw():

    #Initialization for turtle package
    canvaWindow = turtle.Screen()               # this will create an empty window canvas for our digital aquarium
    canvaWindow.setup(width=1024, height=576)   # just force set, but maximize button can change size
    canvaWindow.colormode(255)                  # enable to use RGB mode of color fill
    canvaWindow.bgcolor(17,178,255)             # fill color,light blue color indicate underwater
    draw_pen = turtle.Turtle()                  # we name the turtle: draw_pen, indicate a real pen drawing
    draw_pen.penup()
       
    # drawRectangle(draw_pen,-200,-300,500,500,"black","blue")
    # drawRectangle(draw_pen,0,0,300,300,"yellow","red")
    # drawTriangle(draw_pen,0,0,100,"black","blue",0)
    # drawTriangle(draw_pen,0,100,75,"black","red", "down")
    # drawTriangle(draw_pen,0,0,10,"black","blue")
    # drawTriangle(draw_pen,0,-100,50,"black","red", "left")
    # drawTriangle(draw_pen,0,-200,50,"black","red", "right")
    # drawTriangle(draw_pen,0,100,100,"black","red", "left")
    # drawCircle(draw_pen,0,300,20,"black","red")

    for _ in range(5):
         draw_rock_hexagon(draw_pen,random.randint(-400, 400), -250, 80, "#7B2E0D")
    for _ in range(5):
         draw_rock_octagon(draw_pen,random.randint(-400, 400), -250, 80, "#98411B")

    draw_rock_hexagon(draw_pen,-250, -250, 80, "gray")
    draw_rock_hexagon(draw_pen,-300, -250, 80, "#A9512B")
    draw_rock_hexagon(draw_pen,150, -250, 80, "#BD430F")
    draw_rock_octagon(draw_pen,-150, -250, 80, "#A44116")
    draw_rock_octagon(draw_pen,50, -250, 80, "#47371C")


    draw_octupus(draw_pen,300, 200, 40, '#795458')
    draw_round_fish(draw_pen,100, 200, 50, '#FF8A08')    
    draw_round_fish(draw_pen,-100, 150, 50, '#FF8A08')  
    draw_fish(draw_pen,150, 50, "red")                           # Draw the fish facing left
    draw_fish(draw_pen,-200, -50, "blue", direction="right")     # Draw the fish facing right
    draw_starfish(draw_pen,-200,-200, 30, "#FF9B57")
    
    # seaweed positions
    seaweed_positions = [-200, -100, 100, 150, 200, 300, 320]
    for x in seaweed_positions:
        draw_seaweed(draw_pen,x, -300, 50, "green")

    for _ in range(20): #draw breathing bubbles
        x_axis = random.randint(-500, 500) #random x axis from -500 to 500
        y_axis = random.randint(-300, 300) # random y axis from -300 to 300
        size_circle = random.randint(5,10) # random size 5 to 10
        draw_bubble(draw_pen,x_axis, y_axis, size_circle, "#E1F7F5") 
        
    draw_pen.hideturtle() #make the turtle invisible, so we can view the aquarium
    canvaWindow.exitonclick() 
    

if __name__ == '__main__':
    mainDraw()
