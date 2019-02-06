import turtle
colors = ["red","purple","blue","green","yellow","orange"]
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.width(1)
length = 10

while length < 5000:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length += 4
    
