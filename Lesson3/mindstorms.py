import turtle

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(1, 4):
        some_turtle.forward(100)
        some_turtle.right(-120)

def draw_art():    
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle Brad - Draws a sqaure
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    draw_square(brad)
    #Create the turtle Angie - Draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    #Create the turtle Angie - Draws a triangle
    trigle = turtle.Turtle()
    trigle.shape("turtle")
    trigle.color("yellow")
    draw_triangle(trigle)
    
    window.exitonclick()


draw_art()
