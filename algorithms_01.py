# Чтобы запустить код проскрольте в конец
import turtle


def one(lengthx=100, lengthy=25, n=10):
    for i in range(0, n):
        turtle.forward(lengthx + lengthy * i)
        turtle.right(90)
        if i == n - 1:
            i -= 1
            n -= 1
        turtle.forward(lengthy + lengthy * i)
        turtle.right(90)


def two(timesx=5, timesy=3, step=25):
    turtle.left(90)
    d = step * 2 ** (1/2)
    i = 1
    a = 0
    while True:
        i += 1
        if i <= timesy + 1:
            turtle.forward(step)
            turtle.right(135)
            turtle.forward(d + a)
            a += d
            turtle.left(45)
            turtle.forward(step)
            turtle.left(135)
            turtle.forward(d + a)
            a += d
            turtle.right(45)
        elif i <= timesx + 1:
            turtle.right(90)
            turtle.forward(step)
            turtle.right(45)
            turtle.forward(a)
            turtle.left(45)
            turtle.forward(step)
            turtle.left(135)
            turtle.forward(a)
            turtle.right(45)
        elif i < timesx + timesy + 2:
            turtle.right(90)
            turtle.forward(step)
            turtle.right(45)
            a -= d
            turtle.forward(a)
            turtle.left(135)
            turtle.forward(step)
            turtle.left(45)
            a -= d
            turtle.forward(a)
            turtle.right(45)
        else:
            break


def two_two(step=25):
    turtle.left(90)
    d = step * 2 ** (1/2)
    i = 1
    a = 0

    turtle.forward(step)
    turtle.right(135)
    turtle.forward(d + a)
    a += d
    turtle.left(45)
    turtle.forward(step)
    turtle.left(135)
    turtle.forward(d + a)
    a += d
    turtle.right(45)

    turtle.forward(step)
    turtle.right(135)
    turtle.forward(d + a)
    a += d
    turtle.left(45)
    turtle.forward(step)
    turtle.left(135)
    turtle.forward(d + a)
    a += d
    turtle.right(45)

    turtle.forward(step)
    turtle.right(135)
    turtle.forward(d + a)
    a += d
    turtle.left(45)
    turtle.forward(step)
    turtle.left(135)
    turtle.forward(d + a)
    a += d
    turtle.right(45)

    turtle.right(90)
    turtle.forward(step)
    turtle.right(45)
    turtle.forward(a)
    turtle.left(45)
    turtle.forward(step)
    turtle.left(135)
    turtle.forward(a)
    turtle.right(45)

    turtle.right(90)
    turtle.forward(step)
    turtle.right(45)
    turtle.forward(a)
    turtle.left(45)
    turtle.forward(step)
    turtle.left(135)
    turtle.forward(a)
    turtle.right(45)

    turtle.right(90)
    turtle.forward(step)
    turtle.right(45)
    a -= d
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(step)
    turtle.left(45)
    a -= d
    turtle.forward(a)
    turtle.right(45)

    turtle.right(90)
    turtle.forward(step)
    turtle.right(45)
    a -= d
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(step)
    turtle.left(45)
    a -= d
    turtle.forward(a)
    turtle.right(45)

    turtle.right(90)
    turtle.forward(step)
    turtle.right(45)
    a -= d
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(step)
    turtle.left(45)
    a -= d
    turtle.forward(a)
    turtle.right(45)


def three_addition(high, step, n):
    for i in range(0, n):
        turtle.forward(high)
        turtle.right(90)
        turtle.forward(step)
        turtle.right(90)
        turtle.forward(high)
        if i != n - 1:
            turtle.left(90)
            turtle.forward(step)
            turtle.left(90)


def three(high=200, step=25, n=4, startx=0, starty=0):
    turtle.penup()
    turtle.setx(startx + step/2)
    turtle.sety(starty - high/2)
    turtle.setheading(90)
    turtle.pendown()
    three_addition(high, step, n)
    turtle.penup()
    turtle.setx(startx - step/2)
    turtle.sety(starty + high/2)
    turtle.setheading(270)
    turtle.pendown()
    three_addition(high, step, n)


def four_addition(side, startx, starty):
    turtle.penup()
    turtle.setx(startx - side/2)
    turtle.sety(starty - side/2)
    turtle.setheading(90)
    turtle.pendown()
    for i in range(0, 4):
        turtle.forward(side)
        turtle.right(90)


def four(side=50, step=25, n=10, startx=0, starty=0):
    for i in range(0, n):
        four_addition(side + 2 * i * step, startx, starty)


def five_addition(side, sides):
    turtle.right(180/sides)
    for i in range(0, sides):
        turtle.left(360/sides)
        turtle.forward(side)
    turtle.setheading(90)


def five(side=50, step=10, n=10, startx=0, starty=0):
    turtle.setheading(90)
    turtle.setx(startx)
    turtle.sety(starty)
    for i in range(3, n + 3):
        j = i - 2
        five_addition(side + j * step, i)
        turtle.penup()
        turtle.setx(startx + j * step)
        turtle.pendown()


def six(start_radius=45, step=10, n=10):
    turtle.setheading(90)
    for i in range(0, n):
        turtle.circle(start_radius + i * step)
        turtle.circle(-start_radius - i * step)


if __name__ == '__main__':
    turtle.speed(0)
    turtle.width(2)
    # Запускайте функции тут
    #one()
    two()
    two_two()
    #three()
    #four()
    #five()
    #six()
    turtle.done()
