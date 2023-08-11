from turtle import *
from random import *


def star(x, y):
    Screen().tracer(0, 0)
    
    left(randint(1, 360))
    color = '#' +  ''.join([choice('ABCDEF0123456789') for _ in range(6)])
    quality = randint(5, 11)
    side = randint(7, 30)

    penup()
    goto(x, y)
    pendown()
    pencolor(color)
    pensize(randint(1, 5))
    if choice([True, False]):
        fillcolor(color)
        begin_fill()
        for _ in range(quality):
            forward(side)
            left((quality - 1) // 2 * 360 / quality)
        end_fill()
    else:
        for _ in range(quality):
            forward(side)
            left((quality - 1) // 2 * 360 / quality)
    Screen().update()

Screen().bgcolor(0, 0, 0)

hideturtle()

Screen().onclick(star)
Screen().listen()
done()
