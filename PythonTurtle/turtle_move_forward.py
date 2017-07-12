import turtle

def draw_square():
    window = turtle.screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.forward(100)

    window.exitonClick()

draw_square()
