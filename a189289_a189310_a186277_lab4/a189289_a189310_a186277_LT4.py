'''
Created on April 2024

Some of the function have random integer function,mean every time it run it will produce different result

@author:
Lam Wei Long(A189310)
Izqalan Nor'Izad (A189289)
Nuruddin Naim Bin Abu Hanifah(A186277)
'''
import turtle
import random

def draw_triangle(t,x,y,size,colorP="black",colorF="white", point="up"):
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

# This function is use to draw fish with diamond shape body and triangle tail
# Parameters: draw_pen - turtle object
#             x,y - starting position of the triangle
#             color - fill color
#             facing - the fish facing direction. default is left
# Return: None
def draw_fish(draw_pen,x, y, color, facing="left"):
    draw_pen.penup()
    draw_pen.goto(x, y)
    draw_pen.pendown()
    draw_pen.color(color)
    draw_pen.begin_fill()
    if facing == "left":
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
    elif facing == "right":
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
    if facing == "left":
        draw_pen.goto(x - 30, y + 30)
    elif facing == "right":
        draw_pen.goto(x + 30, y + 30)
    draw_pen.pendown()
    draw_pen.color("black")
    draw_pen.begin_fill()
    draw_pen.circle(5)
    draw_pen.end_fill()
    draw_pen.penup()
    
# This function is use to starfish
# Parameters: draw_pen - turtle object
#             x,y - starting position of the triangle
#             color - fill color
#             facing - the fish facing direction. default is left
# Return: None
def draw_starfish(draw_pen,x, y, size, color):
    draw_pen.penup()
    draw_pen.goto(x, y)
    draw_pen.pendown()
    draw_pen.color(color)
    draw_pen.begin_fill()
    for _ in range(5):
        draw_pen.forward(size)
        draw_pen.right(144)
        draw_pen.forward(size)
        draw_pen.left(72)
    draw_pen.end_fill()
    draw_pen.penup()

def draw_rock_hexagon(draw_pen,x, y, size, color):
    draw_pen.penup()
    draw_pen.goto(x, y)
    draw_pen.pendown()
    draw_pen.color(color)
    draw_pen.begin_fill()
    draw_pen.setheading(random.randint(30, 180))#make it look like rotate instead of fixed angle
    for _ in range(6):
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
    draw_pen.setheading(random.randint(30, 180))#make it look like rotate instead of fixed angle
    for _ in range(8):
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

def draw_submarine(draw_pen, x, y, width, height, color):
    # Draw the submarine body
    draw_pen.penup()
    draw_pen.goto(x, y)
    draw_pen.pendown()
    draw_pen.color(color)
    draw_pen.begin_fill()
    
    # draw pill shape
    draw_pen.left(135)
    for _ in range(2):  # Draw the two halves of the oval
        draw_pen.circle(width, 90)
        draw_pen.circle(height, 90)
    draw_pen.right(45)
    draw_pen.end_fill()

    draw_pen.penup()
    
    # Draw the submarine window

    draw_pen.goto(x - 20, y - 20)
    draw_pen.pendown()
    draw_pen.color("black")
    draw_pen.begin_fill()
    draw_pen.circle(10)
    draw_pen.end_fill()

    draw_pen.goto(x - 60, y - 20)
    draw_pen.pendown()
    draw_pen.color("black")
    draw_pen.begin_fill()
    draw_pen.circle(10)
    draw_pen.end_fill()


    draw_pen.goto(x - 100, y - 20)
    draw_pen.pendown()
    draw_pen.color("black")
    draw_pen.begin_fill()
    draw_pen.circle(10)
    draw_pen.end_fill()
    draw_pen.penup()

    # draw submarine propeller
    draw_pen.goto(x, y)
    draw_pen.pendown()
    draw_pen.color("yellow")
    draw_pen.begin_fill()
    
    draw_triangle(draw_pen, x+10, y-20, 25,"yellow","yellow", "left")

    draw_pen.end_fill()
    draw_pen.penup()

    
             
def mainDraw():

    #Initialization for turtle package
    canvaWindow = turtle.Screen()               # this will create an empty window canvas for our digital aquarium
    canvaWindow.setup(width=1024, height=576)
    # considering every device screen size may different
    # we recommed to run in this fixed size, all the function's x and y cordinate was run in this resolution
    # maximize it may cause the drawing spread apart (for example the rock may not actaully at the bottom of the screen)
    canvaWindow.colormode(255)                  # enable to use RGB mode of color fill
    canvaWindow.bgcolor(17,178,255)             # fill color,light blue color indicate underwater
    draw_pen = turtle.Turtle()                  # we name the turtle: draw_pen, indicate a real pen drawing
    draw_pen.penup()
    draw_pen.speed("fastest")  # Increase drawing speed

    #random rock   
    draw_submarine(draw_pen, -150, 200, 100, 30, "yellow")

    for _ in range(5):
         draw_rock_hexagon(draw_pen,random.randint(-500, 500), -300, 80, "#7B2E0D") 
    for _ in range(5):
         draw_rock_octagon(draw_pen,random.randint(-500, 500), -300, 80, "#98411B")

    draw_rock_octagon(draw_pen,-370, -300, 80, "#45200e")
    draw_rock_hexagon(draw_pen,-300, -300, 80, "#A9512B")
    draw_rock_hexagon(draw_pen,-250, -300, 80, "gray")
    draw_rock_octagon(draw_pen,-150, -300, 80, "#A44116")
    draw_rock_octagon(draw_pen,50, -300, 80, "#47371C")
    draw_rock_hexagon(draw_pen,150, -300, 80, "#BD430F")
    draw_rock_octagon(draw_pen,200, -300, 80, "#b35d12")
    draw_rock_octagon(draw_pen,250, -300, 80, "#8f501a")
    draw_rock_hexagon(draw_pen,300, -300, 80, "#3b1705")
    draw_rock_hexagon(draw_pen,370, -300, 80, "#5e3420")


    draw_octupus(draw_pen,-320, 120, 40, '#ff5200')
    draw_octupus(draw_pen,300, 200, 40, '#795458')
    draw_round_fish(draw_pen,100, 200, 50, '#FF8A08')   
    draw_round_fish(draw_pen,-100, 150, 50, '#FF8A08')  
    draw_fish(draw_pen,150, 50, "red")                           # Draw the fish facing left
    draw_fish(draw_pen,-200, -50, "blue", direction="right")     # Draw the fish facing right
    draw_starfish(draw_pen,-200,-200, 30, "#FF9B57")
    draw_starfish(draw_pen,250,-200, 30, "#e65309")
    
    # seaweed positions
    seaweed_positions = [-300,-270,-100,0, 100, 150, 200, 300, 320]
    for x in seaweed_positions:
        draw_seaweed(draw_pen,x, -300, 50, "green")

    for _ in range(20): 
        x_axis = random.randint(-500, 500) #random x axis from -500 to 500
        y_axis = random.randint(-300, 300) # random y axis from -300 to 300
        size_circle = random.randint(5,10) # random size 5 to 10
        draw_bubble(draw_pen,x_axis, y_axis, size_circle, "#E1F7F5") #draw breathing bubbles
        
    draw_pen.hideturtle() #make the turtle invisible, so we can view the aquarium
    canvaWindow.exitonclick() 
    

if __name__ == '__main__':
    mainDraw()
