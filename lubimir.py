from turtle import *


shape("turtle")
speed(1000)


def background():
    color("black")
    width(800)
    forward(250)

    up()
    right(90)
    forward(160)
    right(90)
    down()

    color("gray")
    width(30)
    forward(500)

    color("white")
    up()
    right(90)
    forward(300)
    right(90)
    forward(50)
    down()

    width(5)
    forward(0)

    up()
    forward(50)
    right(90)
    forward(50)
    left(90)
    down()

    forward(0)

    up()
    forward(50)
    left(90)
    forward(25)
    right(90)
    down()

    forward(0)

    up()
    forward(50)
    left(90)
    forward(30)
    right(90)
    down()

    forward(0)

    up()
    forward(50)
    right(90)
    forward(40)
    left(90)
    down()

    forward(0)

    up()
    forward(50)
    left(90)
    forward(25)
    right(90)
    down()

    forward(0)

    up()
    forward(50)
    right(90)
    forward(50)
    left(90)
    down()

    forward(0)

    up()
    forward(100)
    left(90)
    forward(40)
    down()

    width(50)
    forward(0)


background()

up()
left(180)
forward(265)
right(90)
forward(447)
right(90)
down()


def house1():
    color("dark gray")
    width(1)
    begin_fill()
    forward(200)
    right(90)
    forward(130)
    right(90)
    forward(200)
    end_fill()


house1()

up()
left(180)
forward(150)
left(90)
forward(10)
down()


def windows():
    color("yellow")
    begin_fill()
    forward(40)
    right(90)
    forward(40)
    right(90)
    forward(40)
    right(90)
    forward(40)
    right(90)
    end_fill()

    up()
    forward(70)
    right(90)
    down()

    begin_fill()
    forward(40)
    left(90)
    forward(40)
    left(90)
    forward(40)
    left(90)
    forward(40)
    right(90)
    end_fill()

    up()
    forward(70)
    right(90)
    down()

    begin_fill()
    forward(40)
    right(90)
    forward(40)
    right(90)
    forward(40)
    right(90)
    forward(40)
    left(90)
    end_fill()

    up()
    forward(70)
    left(90)
    down()

    begin_fill()
    forward(40)
    left(90)
    forward(40)
    left(90)
    forward(40)
    left(90)
    forward(40)
    right(90)
    end_fill()

    up()
    forward(70)
    right(90)
    down()

    begin_fill()
    forward(40)
    right(90)
    forward(40)
    right(90)
    forward(40)
    right(90)
    forward(40)
    right(90)
    end_fill()

    up()
    forward(70)
    right(90)
    down()

    begin_fill()
    forward(40)
    left(90)
    forward(40)
    left(90)
    forward(40)
    left(90)
    forward(40)
    right(90)
    end_fill()


windows()

up()
forward(10)
left(90)
forward(100)
left(90)
down()


def clocktower():
    color("gold")
    begin_fill()
    forward(200)
    right(90)
    forward(100)
    right(90)
    forward(200)
    end_fill()

    up()
    goto(-98, 55)
    left(150)
    down()

    color("dimgray")
    begin_fill()
    forward(98)
    right(118)
    forward(100)
    right(30)
    end_fill()

    up()
    forward(80)
    right(92)
    down()

    color("black")
    forward(110)

    up()
    right(180)
    forward(15)
    right(90)
    down()

    forward(120)

    up()
    left(90)
    forward(15)
    left(90)
    down()

    forward(120)

    up()
    right(90)
    forward(15)
    right(90)
    down()

    forward(120)

    up()
    left(90)
    forward(15)
    left(90)
    down()

    forward(120)

    up()
    right(90)
    forward(15)
    right(90)
    down()

    forward(120)

    up()
    left(90)
    forward(15)
    left(90)
    down()

    forward(120)

    up()
    right(90)
    forward(10)
    right(90)
    down()

    forward(120)

    up()
    left(90)
    forward(5)
    left(90)
    forward(120)
    left(90)
    forward(50)
    right(90)
    forward(40)
    down()

    color("white")
    width(70)
    forward(0)

    color("black")
    width(5)
    forward(0)
    width(1)
    forward(31)
    right(240)
    forward(5)
    left(180)
    forward(5)
    left(290)
    forward(5)
    left(180)
    forward(5)

    up()
    right(230)
    forward(31)
    left(90)
    down()

    forward(20)
    right(240)
    forward(5)
    left(180)
    forward(5)
    left(290)
    forward(5)
    left(180)
    forward(5)

    up()
    right(230)
    forward(20)
    left(90)
    forward(40)
    left(90)
    forward(35)
    left(90)
    down()

    forward(80)

    up()
    left(180)
    forward(80)
    right(90)
    forward(70)
    right(90)
    down()

    forward(80)


clocktower()

up()
left(180)
forward(201)
left(90)
forward(105)
left(90)
down()


def house2():
    color("indianred")
    begin_fill()
    forward(200)
    right(90)
    forward(230)
    right(90)
    forward(200)
    end_fill()


house2()

up()
left(180)
forward(150)
left(90)
forward(10)
down()

windows()

up()
goto(140, 45)
forward(41)
right(90)
down()

windows()

up()
forward(10)
left(90)
forward(200)
down()

exitonclick()