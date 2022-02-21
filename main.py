import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
## Part 1
st1 = (-100,20)
st2 = (-100,-20)
x = random.randrange(1,100)
y = random.randrange(1,100)
michelangelo.pendown()
leonardo.pendown()
michelangelo.forward(x)
leonardo.forward(y)

michelangelo.penup()
leonardo.penup()
michelangelo.goto(st1)
leonardo.goto(st2)
#Part 2
x1 = random.randrange(0,10)
y1 = random.randrange(0,10)
michelangelo.pendown()
leonardo.pendown()

for i in range(10):
  michelangelo.forward(x1)
  leonardo.forward(y1)
  
michelangelo.penup()
leonardo.penup()
michelangelo.goto(st1)
leonardo.goto(st2)

# Part B - complete part B here
michelangelo.clear()
leonardo.clear()
leonardo.hideturtle()
st3 =(0,0)
michelangelo.goto(st3)
#Equilateral Triangle 
michelangelo.pendown()
for i in range(3):
  michelangelo.forward(30)
  michelangelo.left(360/3)
michelangelo.penup()
michelangelo.clear()
michelangelo.goto(st3)

#Square
michelangelo.pendown()
for i in range(4):
  michelangelo.forward(30)
  michelangelo.left(360/4)
michelangelo.penup()
michelangelo.clear()
michelangelo.goto(st3)

#Hexacon
michelangelo.pendown()
for i in range(6):
  michelangelo.forward(30)
  michelangelo.left(360/6)
michelangelo.penup()
michelangelo.clear()
michelangelo.goto(st3)

#Nonagon
michelangelo.pendown()
for i in range(9):
  michelangelo.forward(30)
  michelangelo.left(360/9)
michelangelo.penup()
michelangelo.clear()
michelangelo.goto(st3)

#Dodecagon
michelangelo.pendown()
for i in range(12):
  michelangelo.forward(30)
  michelangelo.left(360/12)
michelangelo.penup()
michelangelo.clear()
michelangelo.goto(st3)


window.exitonclick()
