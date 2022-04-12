from turtle import *

speed(0)
setup(800, 500)
bgcolor("#00778B")

penup()
goto(-400, -80)
pendown()

color("#FFC72C")
begin_fill()
forward(800)
left(90)
forward(167)
left(90)
forward(800)
end_fill()

left(90)
penup()
goto(-400, 250)
pendown()

color("black")
begin_fill()
forward(500)
left(130)
forward(400)
end_fill()

hideturtle()
