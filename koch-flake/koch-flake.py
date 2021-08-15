import turtle
import time

t = turtle.Turtle()
turtle.title("Fiocco di Koch")
t.speed(0)
t.hideturtle()

inverse = False
side = 100
iterations = 3

perimeter = 0

def flake(side, iterations):
    for x in range(4):
        if x == 1:
            t.left(55)
        elif x == 2:
            t.right(110)
        elif x == 3:
            t.left(55)

        if iterations > 0:
            flake(side / 3, iterations - 1)
        else:    
            t.forward(side)
            global perimeter
            perimeter += side

def triangle_flake(side, iterations, inverse):
    t.fillcolor("cyan")
    t.begin_fill()
    for x in range(3):
        if inverse:
            t.left(120)
        flake(side, iterations)
        if not inverse:
            t.right(120)
    t.end_fill()

t.up()
if inverse:
    t.goto(300, -300)
else:
    t.goto(-300, 200)
t.down()

ping = time.perf_counter()
triangle_flake(side, iterations, inverse)
pong = time.perf_counter()

print(f"Time: {pong - ping:0.4f} seconds\nPerimeter: {perimeter}")

turtle.done()