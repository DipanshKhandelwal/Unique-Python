import turtle

''' this moves turtle for a length and then make it turn right for 4 times
    making a square

    even tells us how to configure our turtle like changing its speed ,color
    shape etc'''
def customize_turtle():
    window = turtle.Screen()
    window.bgcolor("red")  

    brad = turtle.Turtle()

    brad.shape("turtle")
    ''' Inputs be like :
        turtle.shape()  { gives classic shape }
        turtle.shape("turtle") { “arrow”, “turtle”, “circle”,
                                “square”, “triangle”, “classic” }'''

    
    brad.color("yellow")
    '''input formats for turtle.shape:-
        fillcolor()
        fillcolor(colorstring) { like "red", "yellow", or "#33cc8c" }
        fillcolor((r, g, b))'''

    
    brad.speed(1)
    '''If input is a number greater than 10 or smaller than 0.5, speed is set to 0. Speedstrings are mapped to speedvalues as follows:

        “fastest”: 0
        “fast”: 10
        “normal”: 6
        “slow”: 3
        “slowest”: 1 '''
    
    
    for _ in range(4):
        brad.forward(100)
        brad.right(90)

    window.exitonclick()

customize_turtle()
