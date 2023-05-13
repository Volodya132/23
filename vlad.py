
from turtle import*
from random import*
def rect(a, b):
    forward(a)
    right(90)
    forward(b)
    right(90)
    forward(a)
    right(90)
    forward(b)
    right(90)

color("dark grey")
begin_fill()

end_fill()
speed(1000)
up()
goto(250, 150)
down()
color("#636363")
begin_fill()
rect(-500, 300)
end_fill()

color("#3e0266")
up()
goto(-220,60)
down()
forward(600)

color("#02664d")
up()
goto(-220,-30)
down()
forward(600)

color("#663602")
up()
goto(-220,-120)
down()
forward(600)

up()
goto(250, 150)
down()


color("#fc0505")
begin_fill()
rect(-20, 300)
end_fill()


color("#050000")
begin_fill()
rect(-500, 60)
end_fill()

hura = Turtle()
ghud = Turtle()
meto = Turtle()

hura.shape("turtle")
ghud.shape("square")
meto.shape("triangle")
meto.color("blue")
hura.color("green")
ghud.color("black")

goto(500, 200)
forward( 100 )
left( 90 )
forward ( 100 )
left( 90 )
forward ( 100 )
left( 90 )
forward ( 100 )
left( 90 )


hura.speed(1000)
hura.up()
hura.goto(-220,-30)

ghud.speed(1000)
ghud.up()
ghud.goto(-220, -120)

meto.speed(1000)
meto.up()
meto.goto(-220, 60)

while hura.xcor() < 230 and ghud.xcor() < 230 and meto.xcor() < 230:
    hura.forward(randint(0,7))
    ghud.forward(randint(0,7))
    meto.forward(randint(0,7))

if hura.xcor() > ghud.xcor() and hura.xcor() > meto.xcor():
    hura.write("I win", font=("Verdana", 35, "bold"))
if ghud.xcor() > hura.xcor() and ghud.xcor() > meto.xcor():
    ghud.write("I win", font=("Verdana", 35, "bold"))
if meto.xcor() > hura.xcor() and ghud.xcor() < meto.xcor():
    meto.write("I win", font=("Verdana", 35, "bold"))

exitonclick()
