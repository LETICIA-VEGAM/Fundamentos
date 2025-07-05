import turtle

ventana = turtle.Screen()
t = turtle.Turtle()

for _ in range(3):
    t.forward(100)
    t.left(120)

time.sleep(5)
ventana.mainloop()