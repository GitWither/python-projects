import turtle
import random
import math

turtle.title("Montecarlo")

t = turtle.Turtle()
t.speed(0)


spari = 400
raggio = 400


global_y = -300

centro_x = 0
centro_y = global_y + raggio

t.up()
t.sety(global_y)
t.down()

t.circle(raggio)
t.setx(raggio)
t.sety(raggio * 2 + global_y)
t.setx(-raggio)
t.sety(global_y)
t.setx(centro_x)

dentro = 0

for sparo in range(spari):
    x = random.randint(-raggio, raggio)
    y = random.randint(global_y, raggio * 2 + global_y)

    t.color("black")
    if (x**2 + y**2 <= raggio**2):
       #t.color("red")
       dentro += 1

    t.up()
    t.setx(x)
    t.sety(y)
    t.down
    t.dot(5)

print(4 * (dentro / spari))




turtle.done()