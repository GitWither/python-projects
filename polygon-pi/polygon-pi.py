import turtle
import math

t = turtle.Turtle()

t.speed("fastest")

angle = 0.1
radius = 200

angolo_c = 0

t.up()
t.setpos(0, -radius)
t.down()
t.circle(radius)
t.up()
t.setpos(0, 0)
t.down()
t.setpos(0, 0)
t.setpos(radius, 0)
t.up()
t.setpos(0, 0)
t.down()

pre_x = radius
pre_y = 0

perimetro = 0

lati = 0
lato = ((radius - (radius * math.cos(math.radians(angle)))) ** 2 + (radius * math.sin(math.radians(angle))) ** 2) ** 0.5

while angolo_c < 361.0:
    lati += 1
    x = math.cos(math.radians(angle)) * radius
    y = math.sin(math.radians(angle)) * radius

    #t.setpos(x, y)

    #t.setpos(pre_x, pre_y)

    pre_x = x
    pre_y = y

    t.setpos(math.cos(math.radians(angolo_c)) * radius, math.sin(math.radians(angolo_c)) * radius)
    t.setpos(0, 0)

    angolo_c += angle

perimetro = lati * lato

print(perimetro / (radius * 2))


turtle.done()