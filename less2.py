import turtle
sides = int(input('Set a number '))

for steps in range(sides):
    turtle.forward(100)
    turtle.right(360/sides)
    for moresteps in range(sides):
        turtle.forward(50)
        turtle.right(360/sides)
