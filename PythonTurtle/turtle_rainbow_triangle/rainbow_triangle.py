import turtle
turtle.speed(0)
l=50
ang=15

colors=['purple','indigo','blue','green','yellow','orange','red']

for i in range(100):
    turtle.color("white",colors[i%7])
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(l)
        turtle.left(120)
    turtle.end_fill()
    l+=2
    turtle.left(ang)

