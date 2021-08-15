import turtle

t = turtle.Turtle()

turtle.title("Pythagora's Tree")

steps = 5
side = 100

t.speed(10000000000)
t.hideturtle()

def calc_hypotenuse(l: float):
    return (pow(l * 0.5, 2) + pow(l * 0.5, 2)) ** 0.5

def draw_polygon(lato, steps):
    ipotenusa = calc_hypotenuse(lato)
    for x in range(0, 5):
        if x == 2 or x == 3:
            t.left(-45)
            t.forward(ipotenusa)

            if (steps > 0):
                t.right(180)


                if (steps == 1):
                    t.fillcolor("green")
                t.begin_fill()

                draw_polygon(ipotenusa, steps - 1)

                t.end_fill()

                t.left(180)

            if x == 2:
                t.left(135)
            elif x == 3:
                t.left(45)
        else:
            t.forward(lato)
            t.left(90)

    

draw_polygon(side, steps)

turtle.done()