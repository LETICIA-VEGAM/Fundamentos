import turtle
t = turtle.Turtle()
t.speed(3)

lados = 5
angulo = 360 / lados

for _ in range(lados):
    t.forward(100)
    t.left(angulo)
time.sleep(5)
turtle.done()