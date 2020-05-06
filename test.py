import turtle as t

t.setup(800, 600, 200, 200)

for i in range(8):
    if i % 2 == 0:
        t.penup()

    t.fd(100)
    t.right(90)
    t.circle(-100, 360 / 8)
    t.right(90)
    t.fd(100)

    if i % 2 == 0:
        t.pendown()
t.done()
