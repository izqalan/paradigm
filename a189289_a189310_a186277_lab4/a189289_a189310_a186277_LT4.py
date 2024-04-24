'''
Created on April 2024

@author:
LAM WEI LONG(A189310)
Izqalan Nor'Izad (A189289)
NURUDDIN NAIM BIN ABU HANIFAH(A186277)
'''

import turtle               # allows us to use the turtles library                                         
wn = turtle.Screen()        # creates a graphics window (canvas)                                                   
                                           
def flower(jane):           # This function is a sample, you can delete it
    for i in range(12):     
        # draw a square
        jane.forward(50)
        jane.left(90)
        jane.forward(50)
        jane.left(90)
        jane.forward(50)
        jane.left(90)
        jane.forward(50)
        jane.left(90) 
        jane.left(30)
                                                                                              
def mainDraw():
    jane = turtle.Turtle()    # you can rename the turtle if you want
    flower(jane)   
 
if __name__ == '__main__':
    mainDraw() 

wn.exitonclick()
