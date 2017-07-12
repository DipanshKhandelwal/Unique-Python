import turtle

''' this moves turtle to make a square
    even tells us how to configure our turtle like changing its speed ,color
    shape etc'''

def turtle_circle():
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
    
    brad.circle(120)
    window.exitonclick()

turtle_circle()
