import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
turtle_instance.pensize(1)
turtle_instance.speed(0)

turtle_colors = ["dark red","red","orange","yellow","dark green", "green","light green","dark blue","blue","light blue","purple"]

for i in range(144):
    turtle_instance.circle(5 * i)
    turtle_instance.color(turtle_colors[i % 11])
    turtle_instance.circle(-5 * i)
    turtle_instance.left(5)
    turtle_instance.color(turtle_colors[i % 11])

turtle.mainloop()
turtle.done()