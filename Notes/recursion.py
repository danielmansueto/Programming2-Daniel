# recursion (functions calling themselves)

# functions can call functions
def f():
    print("f")
    g()

def g():
    print("g")

f()

# function calling itself
def f():
    print("F")
    f()
#f()

# we can control the recursion depth
def controlled(level, end_level):
    print("Recursion level:", level)
    if level < end_level:
        controlled(level + 1, end_level)
    print("Level", level, "closed")

controlled(0, 10)

import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.width(3)
my_turtle.shape("turtle")
my_screen = turtle.Screen()

'''
my_turtle.goto(0, 0)
my_turtle.goto(100, 0)
my_turtle.goto(100, 100)

my_turtle.pencolor("blue")
my_turtle.forward(100)  # driving the turtle
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.right(45)
my_turtle.backward(50)

my_turtle.penup()
my_turtle.goto(0, 0)
my_turtle.pendown()
my_turtle.setheading(90)  # turn to the heading (0 right, 180 left)

# draw a shape
my_turtle.fillcolor("red")
my_turtle.pencolor("black")

my_turtle.begin_fill()

for i in range(8):
    my_turtle.forward(50)
    my_turtle.right(360 / 8)

my_turtle.end_fill()

distance = 20
for i in range(500):
    my_turtle.forward(distance + i)
    my_turtle.right(i + 1)
'''

def rect_recursive(width, height, depth, line_width=3):
    if depth > 0:
        my_turtle.pensize(line_width)
        my_turtle.penup()
        my_turtle.goto(-width / 2, height / 2)
        my_turtle.pendown()
        my_turtle.pencolor("purple")
        my_turtle.setheading(0)
        for i in range(2):
            my_turtle.forward(width)
            my_turtle.right(90)
            my_turtle.forward(height)
            my_turtle.right(90)
        rect_recursive(width * 1.25, height * 1.25, depth - 1, line_width * 1.25)

def bracket_recursion(x, y, size, depth):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(90)
    my_turtle.forward(size)
    my_turtle.right(90)
    my_turtle.forward(100)  # make this constant
    pos1 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(-90)
    my_turtle.forward(size)
    my_turtle.left(90)
    my_turtle.forward(100)
    pos2 = my_turtle.pos()

    if depth > 0:
        x, y = pos1
        bracket_recursion(x, y, size * .5, depth - 1)
        x, y = pos2
        bracket_recursion(x, y, size * .5, depth - 1)

#rect(200,100)
#rect_recursive(15, 50, 20, line_width=1)
#bracket_recursion(-250, 0, 150, 5)

def tree(length, n):
    if length < (length / n):
        return
    turtle.forward(length)
    turtle.left(45)
    tree(length * 0.5, length / n)
    turtle.left(20)
    tree(length * 0.5, length / n)
    turtle.right(75)
    tree(length * 0.5, length / n)
    turtle.right(20)
    tree(length * 0.5, length / n)
    turtle.left(30)
    turtle.backward(length)
    return


turtle.left(90)
turtle.backward(30)
tree(200, 4)


my_screen.exitonclick()