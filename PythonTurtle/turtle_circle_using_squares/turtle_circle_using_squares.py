import turtle

'''this makes a circle by building many squares'''
def draw_square(tom):
    for _ in range(4):
        tom.forward(100)
        tom.right(90)

def draw_circle_using_squares():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.speed(0)

    for i in range(72):
        draw_square(brad)
        brad.right(5)

    window.exitonclick()

draw_circle_using_squares()
