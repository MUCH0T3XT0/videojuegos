import random
import turtle

# Importing everything with * is not a good practice, it's preferable to import only what's necessary

from freegames import path

# Declaring all imports at the beginning of the file is a good practice

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0

# Using descriptive comments to explain the purpose of variables and functions

def draw_square(x, y):
    """Draws a white square with black outline at (x, y)."""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('black', 'white')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()

# Using descriptive function and variable names

def index_from_coordinates(x, y):
    """Converts (x, y) coordinates to a tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Using docstrings to document function purpose

def coordinates_from_index(count):
    """Converts tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Using comments to explain code logic

def handle_click(x, y):
    """Updates mark and hidden tiles based on click."""
    spot = index_from_coordinates(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


# Function to count and display the number of taps

def display_tap_count():
    """Displays the number of taps."""
    global tap_count
    up()
    goto(-200, -220)
    color('black')
    write(f"Taps: {tap_count}", font=('Arial', 16, 'normal'))
    update()

# Function to detect when all tiles have been uncovered

def all_tiles_uncovered():
    """Checks if all tiles have been uncovered."""
    return all(not tile_hidden for tile_hidden in hide)

# Ensuring a clear and organized structure of the code

def draw():
    """Draws the image and tiles."""
    turtle.clear()
    turtle.goto(0, 0)
    turtle.shape(car)
    turtle.stamp()

    for count in range(64):
        if hide[count]:
            x, y = coordinates_from_index(count)
            draw_square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = coordinates_from_index(mark)
        turtle.up()
        turtle.goto(x + 2, y)
        turtle.color('black')
        turtle.write(tiles[mark], font=('Arial', 30, 'normal'))

    turtle.update()
    turtle.ontimer(draw, 100)

# Following naming conventions and using descriptive names for functions

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(handle_click)
draw()
done()

# Commit message: Added functions to count taps and detect when all tiles are uncovered
