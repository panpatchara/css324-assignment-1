def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s == (4, 4, 0)

def successors(s):
    x, y, z = s
    t = 5 - y
    
    if x > 0 and t > 0:
        if x > t:
            yield ((x - t, 5, z), t)
        else:
            yield ((0, y + x, z), x)
    #pour y to x
    t = 8 - x
    if y > 0 and t > 0:
        if y > t:
            yield ((8, y - t, z), t)
        else:
            yield ((x + y, 0, z), y)
    #pour x to z
    t = 3 - z
    if x > 0 and t > 0:
        if x > t:
            yield ((x - t, y, 3), t)
        else:
            yield ((0, y, z + x), x)
    #pour z to x
    t = 8 - x
    if z > 0 and t > 0:
        if z > t:
            yield ((8, y, z - t), t)
        else:
            yield ((x + z, y, 0), z)
    #pour z to y
    t = 5 - y
    if z > 0 and t > 0:
        if z > t:
            yield ((x, y - t, z - t), t)
        else:
            yield ((x, 0, y + z), z)
    #pour y to z
    t = 3 - z
    if y > 0 and t > 0:
        if y > t:
            yield ((x, y-t, 3), t)
        else:
            yield ((x, 0, z + y), y)
