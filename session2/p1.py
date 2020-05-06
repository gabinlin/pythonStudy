import turtle as t

t.setup(600, 400, 200, 200)

t.penup()
t.fd(-250)
t.pendown()

t.seth(-40)
t.pensize(25)
t.pencolor('red')

for i in range(4):
    t.circle(40, 80)
    t.circle(-40, 80)
t.pencolor('blue')
t.circle(40, 80/2)
t.pencolor('red')
t.fd(40)
t.pencolor('yellow')
t.circle(16, 180)
t.pencolor('blue')
t.fd(40 * 2/3)

t.done()
