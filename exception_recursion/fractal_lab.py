#Turtle Recursion (25pts)

#1)  Using the turtle library, create the H fractal pattern according to the file shown in the data folder. (10pts)
import turtle
print()
print("Problem #1:")
print()

my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.width(2)
my_turtle.shape("turtle")
my_screen = turtle.Screen()

def Hfractal(x, y, size, depth):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(0)
    my_turtle.forward(size / 2)
    my_turtle.right(90)
    my_turtle.forward(size / 2)
    pos3 = my_turtle.pos()
    my_turtle.backward(size)
    pos1 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(180)
    my_turtle.forward(size / 2)
    my_turtle.left(90)
    my_turtle.forward(size / 2)
    pos4 = my_turtle.pos()
    my_turtle.backward(size)
    pos2 = my_turtle.pos()



    if depth > 0:
        x, y = pos1
        Hfractal(x, y, size * .5, depth - 1)
        x, y = pos2
        Hfractal(x, y, size * .5, depth - 1)
        x, y = pos3
        Hfractal(x, y, size * .5, depth - 1)
        x, y = pos4
        Hfractal(x, y, size * .5, depth - 1)


#Hfractal(0, 0, 300, 3)



#2)  Using the turtle library, create any of the other recursive patterns in the data folder. 
#  Challenge yourself to match your pattern as closely as you can to the image.  (10pts)
#  Note:  The Koch snowflake shows step by step building of the fractal.  
#  The rectangle fractal example shows 4 possible drawings of the same fractal (choose any one)

def snowflake_fractal(x, y, size, depth):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(90)
    my_turtle.right(30)

    my_turtle.right(60)
    my_turtle.forward(size)
    mypos1 = my_turtle.pos()
    my_turtle.backward(size)

    my_turtle.right(60)
    my_turtle.forward(size)
    mypos2 = my_turtle.pos()
    my_turtle.backward(size)

    my_turtle.right(60)
    my_turtle.forward(size)
    mypos3 = my_turtle.pos()
    my_turtle.backward(size)

    my_turtle.right(60)
    my_turtle.forward(size)
    mypos4 = my_turtle.pos()
    my_turtle.backward(size)

    my_turtle.right(60)
    my_turtle.forward(size)
    mypos5 = my_turtle.pos()
    my_turtle.backward(size)

    my_turtle.right(60)
    my_turtle.forward(size)
    mypos6 = my_turtle.pos()
    my_turtle.backward(size)

    if depth > 0:
        x, y = mypos1
        snowflake_fractal(x, y, size * .3, depth - 1)

        x, y = mypos2
        snowflake_fractal(x, y, size * .3, depth - 1)

        x, y = mypos3
        snowflake_fractal(x, y, size * .3, depth - 1)

        x, y = mypos4
        snowflake_fractal(x, y, size * .3, depth - 1)

        x, y = mypos5
        snowflake_fractal(x, y, size * .3, depth - 1)

        x, y = mypos6
        snowflake_fractal(x, y, size * .3, depth - 1)

# snowflake_fractal(0, 0, 200, 3)


#3)  Create your own work of recursive art with a repeating pattern of your making (or choose another one from the files).  
#  It must be a repeated pattern using recursion (not just loops). Snowflakes, trees, and spirals are a common choice.  
#  Play around and have fun with it.  (5pt) 

#  General expectations for all problems
#  Give all your fractals a depth of at least 4.  (Don't make programs that take forever though)  
#  Ensure the recursive drawing is contained on the screen (at whatever size you set it).
#  All three recursive drawings can be on the same program.  Just use screen.clear() between problems.  Alternately, you could draw to three different screen objects.
#  Run your turtles at max speed.
#  Have fun!
 
#  Resource to help you out >>> https://docs.python.org/3.3/library/turtle

my_turtle.left(90)

lv = 11
s  = 17

my_turtle.penup()
my_turtle.backward(100)
my_turtle.pendown()
my_turtle.forward(100)

def tree(size, depth):
    size = 3 / 4 * size
    my_turtle.left(s)
    my_turtle.forward(size)
    depth += 1
    if depth < lv:
        tree(size, depth)

    my_turtle.backward(size)
    my_turtle.right(2*s)
    my_turtle.forward(size)
    if depth <= lv:
        tree(size, depth)
    my_turtle.backward(size)
    my_turtle.left(s)
    depth -= 1

tree(100, 3)

my_screen.exitonclick()
