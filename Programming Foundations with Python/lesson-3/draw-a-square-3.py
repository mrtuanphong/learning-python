import turtle

def draw_square(_turtle):
    for i in range(1,5):
        _turtle.forward(100)
        _turtle.right(90)
    
def draw_art():
    window = turtle.Screen()
    window.bgcolor("orange")

    #draw square:
    brad = turtle.Turtle()
    brad.color("red")
    brad.shape("turtle")
    brad.speed(20)

    for i in range(1, 37):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()
    
draw_art()
