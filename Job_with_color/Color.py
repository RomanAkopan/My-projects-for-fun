from turtle import *
from random import  randint, random

tracer(20)
bgcolor("black")
tracer(100)
pensize(1)

for _ in range(500):
    x = randint(-300, 300)
    y = randint(-300, 300)
    size = randint(2, 10)
    up()
    goto(x, y)
    down()
    color(random(), random(), random())
    begin_fill()
    for _ in range(5):
        forward(size)
        right(144)
end_fill()
done()