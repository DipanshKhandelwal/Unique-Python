import turtle


''' code to open a new window and print a straight line '''
def move_forward():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.forward(100)

    window.exitonClick()

move_forward()
