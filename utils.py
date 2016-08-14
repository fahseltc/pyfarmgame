import math

def grid_distance(source, target):
    a = (target[0] - source[0]) ** 2
    b = (target[1] - source[1]) ** 2

    return math.sqrt(a + b)