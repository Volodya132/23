from turtle import *
speed(200)
shape("turtle")
def draw(x,y):
    penup()
    goto(x,y)
    pendown()
def move(length1,angle1,length2,angle2):
    forward(length1)
    right(angle1)
    forward(length2)
    left(angle2)

color('slate gray')
pensize(2233)
forward(2)
up()

goto(-250,-100)
pensize(2)
down()
left(90)
begin_fill()
color('black')
move(40,90,10,90)
forward(20)
right(90)
move(30,90,10,90)
move(10,90,10,90)
forward(10)

# second building
left(90)
forward(20)
right(90)
move(20,90,20,90)
forward(10)
left(90)

# third building
forward(30)
right(90)
forward(4)
circle(3)
move(4,90,4,90)



# 4th building
move(5,90,2,90)
forward(5)
left(90)
move(7,90,10,90)
move(10,90,6,90)
move(20,90,3,90)
move(10,90,3,90)
forward(5)
right(90)
move(10,90,5,90)
move(3,90,10,90)
move(3,90,20,90)
move(6,90,20,90)
move(3,90,5,90)
move(4,90,8,90)

#between 4th building and Empire state building

forward(7)
left(90)
move(9,90,10,90)


#Empire State Building

move(10,90,10,90)
move(100,90,5,90)
move(20,90,5,90)
move(15,90,2,90)
move(10,90,10,90)


# top of ESB

move(10,90,20,95)
move(90,190,89,95)
move(20,90,10,90)
move(10,90,10,90)
move(2,90,15,90)
move(5,90,20,90)
move(5,90,142,90)

#between Empire and Chrysler
forward(4)
left(90)
forward(90)
right(90)
move(50,90,4,90)
forward(6)
right(90)
goto(125,-20)

#Chrysler
left(90)
forward(20)
left(90)
move(12,90,4,90)
forward(12)
right(90)
forward(4)
goto(160,30)
left(88)
forward(20)
left(180)
forward(20)
forward(25)
left(90)
move(4,90,12,90)
move(4,90,15,90)
move(4,90,60,90)
forward(4)
left(90)
forward(40)
right(90)
move(10,90,10,90)
forward(15)
right(90)
forward(50)
end_fill()

up()
goto(-250,-100)
pensize(2)
down()

left(182)
color('white')
move(40,90,10,90)
forward(20)
right(90)
color('dark gray')
move(30,90,10,90)
move(10,90,10,90)
forward(10)

# second building
left(90)
forward(20)
right(90)
color('white')
move(20,90,20,90)
forward(10)
left(90)

# third building
forward(30)
right(90)
forward(4)
color('dark gray')
circle(3)
move(4,90,4,90)



# 4th building
color('white')
move(5,90,2,90)
forward(5)
left(90)
move(7,90,10,90)
move(10,90,6,90)
move(20,90,3,90)
color('dark gray')
move(10,90,3,90)
forward(5)
right(90)
move(10,90,5,90)
move(3,90,10,90)
move(3,90,20,90)
move(6,90,20,90)
move(3,90,5,90)
move(4,90,8,90)

#between 4th building and Empire state building

forward(7)
color('dark gray')
left(90)
move(9,90,10,90)


#Empire State Building
color('white')
move(10,90,10,90)
move(100,90,5,90)
move(20,90,5,90)
move(15,90,2,90)
color('dark gray')
move(10,90,10,90)


# top of ESB
color('white')
move(10,90,20,95)
move(90,190,89,95)
color('dark gray')
move(20,90,10,90)
move(10,90,10,90)
move(2,90,15,90)
move(5,90,20,90)
move(5,90,142,90)

#between Empire and Chrysler
color('white')
forward(4)
left(90)
forward(90)
right(90)
color('dark gray')
move(50,90,4,90)
forward(6)
right(90)
goto(125,-20)

#Chrysler
color('white')
left(90)
forward(20)
left(90)
move(12,90,4,90)
forward(12)
color('dark gray')
right(90)
forward(4)
goto(160,30)
left(88)
forward(20)
left(180)
forward(20)
forward(25)
left(90)
move(4,90,12,90)
move(4,90,15,90)
move(4,90,60,90)
color('white')
forward(4)
left(90)
forward(40)
right(90)
color('dark gray')
move(10,90,10,90)
forward(15)
right(90)
forward(50)

#stars
color('white')
up()
goto(-100,200)
down()
circle(1)

up()
goto(-200,190)
down()
circle(1)

up()
goto(-210,100)
down()
circle(1)

up()
goto(-254,150)
down()
circle(1)

up()
goto(100,200)
down()
circle(1)

up()
goto(200,190)
down()
circle(1)

up()
goto(210,100)
down()
circle(1)

up()
goto(254,150)
down()
circle(1)

up()
goto(43,165)
down()
circle(1)

up()
goto(-70,56)
down()
circle(1)

up()
goto(-43,165)
down()
circle(1)

up()
goto(23,50)
down()
circle(1)

#moon
up()
goto(50,100)
down
begin_fill()
circle(20)
end_fill()

up()
goto(-250,-100)
down()

up()
goto(2133,43443)

exitonclick()
