import turtle

# draw a shape:
def draw_square(_turtle):
    _turtle.forward(100)
    _turtle.right(60)
    _turtle.forward(100)
    _turtle.right(60*2)    
    _turtle.forward(100)
    _turtle.right(60)
    _turtle.forward(100)

def draw_leaf(_turtle):
    # right leaf:
    _turtle.left(15)
    _turtle.forward(100)
    _turtle.right(30)
    _turtle.forward(100)
    _turtle.right(180 - 30)
    _turtle.forward(100)
    _turtle.right(30)
    _turtle.forward(100)
    # left leaf:
    _turtle.forward(100)
    _turtle.left(30)
    _turtle.forward(100)
    _turtle.left(180 - 30)
    _turtle.forward(100)
    _turtle.left(30)
    _turtle.forward(100)

def draw_art():
    # create a window:
    window = turtle.Screen()
    window.bgcolor("red")
    
    # create a turtle:
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed(0)

    # the turtle starts drawing:
    for i in range(1, 73):
        draw_square(brad)
        brad.right(5)

    # the turtle finishs drawing the flower:
    brad.right(90)
    brad.forward(220)
    brad.left(90)
    
    # drawing the leaves:
    draw_leaf(brad)
    brad.right(90 + 15)
    brad.forward(60)
    
    # click on window to exit:
    window.exitonclick()

# run program
draw_art()
