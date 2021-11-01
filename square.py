import turtle

wn = turtle.Screen()
Kenny = turtle.Turtle()

sides = input("Number of sides in polygon?")
length = input("Length of the sides in polygon?")
colorname = input("Color of polygon?")
fcolor = input("Fill color of polygon?")

Kenny.color = (colorname)
Kenny.fillcolor = (fcolor)

for i in range(sides):
    Kenny.forward(length)
    Kenny.left(360 / sides)