import turtle

ventana = turtle.Screen()
t = turtle.Turtle()

t.speed(1)

ancho = 100
alto = 100

for _ in range(2):
    t.forward(ancho)
    t.left(90)
    t.forward(alto)
    t.left(90)
    
time.sleep(5)
ventana.mainloop()