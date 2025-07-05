import turtle

wn = turtle.Screen()
wn.title("Hexágono con Turtle")

t = turtle.Turtle()

for _ in range(6):
    t.forward(100)
    t.right(60)
time.sleep(5)
wn.mainloop()