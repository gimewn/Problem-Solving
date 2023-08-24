def solution(park, routes):
    def is_can_do(op, count):
        nonlocal sx, sy
        for c in range(1, count+1):
            dx, dy = sx + direction[op][0]*c, sy + direction[op][1]*c
            if 0 > dx or dx >= X or 0 > dy or dy >= Y:
                return False
            if park[dx][dy] == 'X':
                return False
        sx, sy = dx, dy
        return True

    X = len(park)
    Y = len(park[0])
    
    direction = {
        'E' : (0, 1),
        'W' : (0, -1),
        'S' : (1, 0),
        'N' : (-1, 0)
    }
    
    sx, sy = -1, -1
    
    for x in range(X):
        if sx != -1 and sy != -1:
            break
        for y in range(Y):
            if park[x][y] == 'S':
                sx, sy = x, y
                break
    
    for route in routes:
        dir, count = route.split(" ")
        is_can_do(dir, int(count))
    
    return [sx, sy]