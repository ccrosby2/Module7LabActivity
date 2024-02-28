#Cierra Crosby
#Instructor Nathan Braun
#2/28/2024
#Module 7 Problem 5
#This program use the following an example code of turtle statement as a base to produce an image of four squares.

import turtle

def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

for i in range(5):
	draw_square(alex,40*(i+1))
	alex.penup()
	alex.backward(20)
	alex.right(90)
	alex.forward(20)
	alex.left(90)
	alex.pendown()
	
wn.exitonclick()