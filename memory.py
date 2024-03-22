from random import *
from turtle import *


# Importar todo con * no es una buena práctica, es preferible importar solo lo necesario


from freegames import path


# Declarar todas las importaciones al principio del archivo es una buena práctica


car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64


# Es una buena práctica utilizar comentarios descriptivos para explicar el propósito de las variables y funciones

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


# Es recomendable utilizar nombres de funciones y variables descriptivos


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Se pueden utilizar docstrings para documentar el propósito de las funciones

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Es recomendable utilizar comentarios para explicar la lógica del código

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
tap_count = 0


# Es importante tener una estructura clara y organizada del código

def draw():
    """Draws the image and tiles."""
    global tap_count
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

# Es importante seguir convenciones de nomenclatura y utilizar nombres descriptivos para las funciones

def square(x, y):
    """Draws a white square with a black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Converts (x, y) coordinates to a tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Converts tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Updates mark and hidden tiles based on click."""
    global tap_count
    tap_count += 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    print("Number of taps:", tap_count)

    if all_tiles_uncovered():
        print("All tiles have been uncovered!")


def all_tiles_uncovered():
    """Checks if all tiles have been uncovered."""
    return all(not tile_hidden for tile_hidden in hide)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
