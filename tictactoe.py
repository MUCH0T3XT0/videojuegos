"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""
# Import libraries
import turtle
from freegames import line


# Make the grid of the game
def grid():
    """Set grid color"""
    turtle.color("green")
    """Draw the grid"""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


# Draw the X player
def drawx(x, y):
    """Set X color"""
    turtle.color("yellow")
    """Draw X figure"""
    line(x + 33, y + 33, x + 101, y + 101)
    line(x + 33, y + 101, x + 101, y + 33)


# Draw the O player
def drawo(x, y):
    """Set O color"""
    turtle.color("blue")
    """Draw O figure"""
    turtle.up()
    turtle.goto(x + 67, y + 27)
    turtle.down()
    turtle.circle(40)


# Define the game floor
def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]
used_positions = []


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    """Check if the box has already been taken"""
    if (x, y) in used_positions:
        print("Already taken, take another one")
        return
    draw = players[player]
    draw(x, y)
    turtle.update()
    state['player'] = not player
    used_positions.append((x, y))


turtle.setup(420, 420, 370, 0)
# Set the background color
turtle.bgcolor('black')
# Activate the grid and turtle functions
turtle.hideturtle()
turtle.tracer(False)
grid()
turtle.update()
turtle.onscreenclick(tap)
turtle.done()
