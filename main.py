import turtle
import random
import time
from pygame import mixer

# Adding music is optional as per your choice.
#mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
#mixer.init()
#mixer.music.load("/home/Downloads/happy-birthday-song.mp3") #add your music file name or path

# sets background
bg = turtle.Screen()
bg.bgcolor("light green")
#mixer.music.play()


# Bottom Line 1
turtle.penup()
turtle.goto(-170,-180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)

# Mid Line 2
turtle.penup()
turtle.goto(-160,-150)
turtle.color("white")
turtle.pendown()
turtle.forward(300)

# First Line 3
turtle.penup()
turtle.goto(-150,-120)
turtle.color("white")
turtle.pendown()
turtle.forward(250)
bg.bgcolor("grey")

# Cake
turtle.penup()
turtle.goto(-100,-100)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()
bg.bgcolor("pink")

# Candles
turtle.penup()
turtle.goto(-90,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-60,0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-30,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(0,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(30,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)
bg.bgcolor("black")

# Decoration
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

bg.bgcolor("black")

# Happy Birthday message

turtle.penup()
turtle.goto(-200, 50)
turtle.color("lightBlue")
turtle.pendown()

# ENTER YOUR NAME IN THE NAME PLACE
turtle.write(arg="Happy Birthday Shiva Anna !", align="left", font=("roboto", 24, "normal"))

time.sleep(5)