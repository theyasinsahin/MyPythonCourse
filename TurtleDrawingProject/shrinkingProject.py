import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
turtle_instance.pensize(5)
turtle_instance.speed(30)

def DrawSquare(len):
    for i in range(160):
        turtle_instance.forward(len)
        turtle_instance.right(90)
        len = len - 5

DrawSquare(800)
turtle.done()