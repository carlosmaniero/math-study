import math
from collections import namedtuple


Coords = namedtuple('Coords', 'x y')


def get_coords():
    x, y = input("[x, y]: ").split()
    return Coords(float(x), float(y))

v = [get_coords(), get_coords()]
v = [v[0].x - v[1].x, v[0].y - v[1].y]


print(math.sqrt(v[0] ** 2 + v[1] ** 2))
