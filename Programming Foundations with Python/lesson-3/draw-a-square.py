# Steps:
# 1. Move forward -> Turn right
# 2. Move forward -> Turn right
# 3. Move forward -> Turn right
# 4. Move forward -> Turn right

import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("orange")
    
    brad = turtle.Turtle()
    brad.color("red")
    brad.shape("turtle")
    brad.speed(1)
    
    #1:
    brad.forward(100)
    brad.right(90)
    #1:
    brad.forward(100)
    brad.right(90)
    #3:
    brad.forward(100)
    brad.right(90)
    #4:
    brad.forward(100)
    brad.right(90)

    #new shape:
    angie = turtle.Turtle()
    angie.color("blue")
    angie.shape("arrow")
    angie.circle(100)

    window.exitonclick()
    
draw_square()
