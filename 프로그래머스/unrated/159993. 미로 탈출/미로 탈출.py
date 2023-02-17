from collections import deque

def solution(maps):
    answer = 0
    ylength = len(maps)
    xlength = len(maps[0])
    sy, sx = 0, 0
    ey, ex = 0, 0
    ly, lx = 0, 0

    def BFS(sy, sx, ty, tx):
        check = [[True] * xlength for _ in range(ylength)]
        q = deque()
        q.append((sy, sx, 0))
        check[sy][sx] = False

        while q:
            ny, nx, ncount = q.popleft()

            if ny == ty and nx == tx:
                return ncount

            for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                dy, dx = ny + i, nx + j
                if 0 <= dy < ylength and 0 <= dx < xlength:
                    if maps[dy][dx] != 'X' and check[dy][dx]:
                        check[dy][dx] = False
                        q.append((dy, dx, ncount + 1))
        
        return -1

    for y in range(ylength):
        for x in range(xlength):
            if maps[y][x] == 'S':
                sy, sx = y, x
            elif maps[y][x] == 'E':
                ey, ex = y, x
            elif maps[y][x] == 'L':
                ly, lx = y, x

    s_to_l = BFS(sy, sx, ly, lx)
    l_to_e = BFS(ly, lx, ey, ex)
    
    if s_to_l > 0 and l_to_e > 0:
        answer = s_to_l + l_to_e
    else:
        answer = -1
    
    return answer
