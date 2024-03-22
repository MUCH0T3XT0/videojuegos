import random
import turtle


from freegames import path


car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64


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


def index_from_coordinates(x, y):
    """Converts (x, y) coordinates to a tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def coordinates_from_index(count):
    """Converts tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


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


random.shuffle(tiles)
turtle.setup(420, 420, 370, 0)
turtle.addshape(car)
turtle.hideturtle()
turtle.tracer(False)
turtle.onscreenclick(handle_click)
draw()
turtle.done()
