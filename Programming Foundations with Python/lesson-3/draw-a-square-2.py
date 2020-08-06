# Steps:
# 1. Move forward -> Turn right
# 2. Move forward -> Turn right
# 3. Move forward -> Turn right
# 4. Move forward -> Turn right

import turtle

def draw_square(my_turtle):
    for i in range(1,5):
        my_turtle.forward(100)
        my_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("orange")

    #draw square:
    brad = turtle.Turtle()
    brad.color("red")
    brad.shape("turtle")
    brad.speed(1)
    draw_square(brad)
    
    #draw circle:
    angie = turtle.Turtle()
    angie.color("blue")
    angie.shape("arrow")
    angie.circle(100)

    window.exitonclick()
    
draw_art()
