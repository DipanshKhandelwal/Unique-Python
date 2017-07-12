import turtle

''' this moves turtle and makes a triangle'''
def turtle_triangle():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)

    for _ in range(3):
        brad.right(60)
        brad.forward(200)
        brad.right(60)

    window.exitonclick()

turtle_triangle()
