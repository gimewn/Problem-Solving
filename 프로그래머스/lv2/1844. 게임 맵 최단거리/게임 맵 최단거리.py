from collections import deque

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(Y, X, map):
    q = deque()
    q.append((0, 0, 0)) # y, x, cnt
    check = [[0]*X for _ in range(Y)]
    check[0][0] = 1
    while q:
        ny, nx, ncnt = q.popleft()

        if ny == Y-1 and nx == X-1:
            return ncnt+1

        for i, j in dir:
            dy, dx = ny+i, nx+j
            if 0 <= dy < Y and 0 <= dx < X:
                if check[dy][dx]:continue
                if map[dy][dx] == 0: continue
                check[dy][dx] = 1
                q.append((dy, dx, ncnt+1))
    return -1

def solution(maps):
    answer = 0
    Y = len(maps)
    X = len(maps[0])

    answer = BFS(Y, X, maps)
    return answer