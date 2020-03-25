'''
Turtle Recursion (30pts)

1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)

2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)

3)  Create your own work of art with a repeating pattern of your making.  It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.  Or you can create a third one from the directory. (5pt)


 Each fractal should
 - be recursive
 - have a depth of at least 4
 - be contained on the screen

  Have fun!

'''

import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(0)

my_screen = turtle.Screen()
my_screen.bgcolor('white')


def recursive_h(x, y, width, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x - (width / 2), y + (height / 2))
        my_turtle.down()
        my_turtle.goto(x - (width / 2), y - (height / 2))
        my_turtle.goto(x - (width / 2), y)
        my_turtle.goto(x + (width / 2), y)
        my_turtle.goto(x + (width / 2), y + height / 2)
        my_turtle.goto(x + (width / 2), y - height / 2)
        my_turtle.up()
        my_turtle.goto(x, y)
        recursive_h(x + width / 2, y + height / 2, width // 2, height // 2, depth - 1)
        recursive_h(x + width / 2, y - height / 2, width // 2, height // 2, depth - 1)
        recursive_h(x - width / 2, y - height / 2, width // 2, height // 2, depth - 1)
        recursive_h(x - width / 2 , y + height / 2, width // 2, height // 2, depth - 1)


def recursive_escher_fractal(x, y, head, side, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.setheading(head)
        my_turtle.down()
        for i in range(4):
            my_turtle.forward(side)
            my_turtle.right(90)
            my_turtle.forward(side)
        new_position = my_turtle.pos()
        recursive_escher_fractal(new_position[0], new_position[1], head + 45, side * 45 / 64, depth - 1)


def recursive_personal(x, y, width, height, depth, thickness):
    my_turtle.width(thickness)
    my_turtle.goto(x, y - height)
    my_turtle.goto(x, y)
    if depth > 0:
        my_turtle.width(thickness)
        my_turtle.down()
        my_turtle.goto(x + width, y + height)
        next_position = my_turtle.pos()
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x - width, y + height)
        my_turtle.up()
        my_turtle.goto(next_position)
        my_turtle.setheading(50)
        recursive_personal(x + width, y + height, width / 2, height / 2, depth - 1, thickness - 1)
        recursive_personal(x - width, y + height, width / 2, height / 2, depth - 1, thickness - 1)


recursive_h(0, 0, 300, 400, 4)
my_screen.clear()
recursive_personal(0, 0, 30, 30, 5, 5)
my_screen.clear()
recursive_escher_fractal(-250, 250, 0, 500, 16)

my_screen.exitonclick()