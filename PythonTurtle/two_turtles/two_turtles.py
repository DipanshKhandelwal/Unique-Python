import turtle

''' this moves turtle 1 to make a square
    and then turtle 2 to make a circle'''
def two_turtles():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)


    tom = turtle.Turtle()

    tom.shape("arrow")
    tom.color("blue")
    tom.speed(2)

    for _ in range(4):
        brad.forward(100)
        brad.right(90)

    tom.circle(120)

    window.exitonclick()

two_turtles()
