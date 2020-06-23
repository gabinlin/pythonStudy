#!/usr/bin/python3
import turtle as t

t.setup(800, 300, 0, 0)
t.left(180)
t.penup()
t.fd(100)
t.right(180)
def drawLine(draw):
    t.pendown() if draw else t.penup()
    t.fd(40)
    t.right(90)

def drawDigit(num):
    drawLine(True) if num in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if num in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if num in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if num in [0, 2, 6, 8] else drawLine(False)

    t.left(90)
    drawLine(True) if num in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if num in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if num in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)


def drawDate(date):
    for i in date:
        drawDigit(eval(i))
        t.left(180)
        t.penup()
        t.fd(15)
        t.pendown()

drawDate('20200618')
t.done()