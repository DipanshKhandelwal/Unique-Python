import turtle

'''this makes a circle by building many squares'''
def draw_square(tom):
    for _ in range(4):
        tom.forward(100)
        tom.right(90)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.speed(0)
    brad.color("blue")

    for i in range(72):
        draw_square(brad)
        brad.right(5)

    brad.color("green")
    brad.right(90)
    brad.forward(250)
    brad.right(90)
    brad.forward(3)
    brad.right(90)
    brad.forward(250)

    window.exitonclick()

draw_flower()
