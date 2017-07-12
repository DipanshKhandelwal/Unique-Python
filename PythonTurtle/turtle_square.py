import turtle

''' this moves turtle for a length and then make it turn right for 4 times
    making a square '''
def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()

    for _ in range(4):
        brad.forward(100)
        brad.right(90)

    window.exitonClick()

draw_square()
