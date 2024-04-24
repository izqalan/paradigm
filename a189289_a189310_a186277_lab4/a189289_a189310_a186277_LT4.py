'''
Created on April 2024

@author:
LAM WEI LONG(A189310)
Izqalan Nor'Izad (A189289)
NURUDDIN NAIM BIN ABU HANIFAH(A186277)
'''

import turtle               # allows us to use the turtles library                                         
canvaWindow = turtle.Screen()            # creates a graphics window (canvas)        
                                                                                      
                                                      

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
    
    drawRectangle(draw_pen,-200,-300,500,500,"black","blue")
    drawRectangle(draw_pen,0,0,300,300,"yellow","red")
 
if __name__ == '__main__':
    mainDraw()



canvaWindow.exitonclick()
