import sys
from collections import deque

dir = [(0, 0, -1), (0, 0, 1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

def BFS(board, s, floor_cnt, Y, X):
    q = deque([s])
    sf, sy, sx = s
    check = [[[-1]*X for _ in range(Y)] for _ in range(floor_cnt)]
    check[sf][sy][sx] = 0

    while q:
        nf, ny, nx = q.popleft()
        if board[nf][ny][nx] == 'E':
            return check[nf][ny][nx]

        for i, j, k in dir:
            df, dy, dx = nf+i, ny+j, nx+k
            if 0 <= df < floor_cnt and 0 <= dy < Y and 0 <= dx < X:
                if check[df][dy][dx] != -1 or board[df][dy][dx] == '#':
                    continue
                check[df][dy][dx] = check[nf][ny][nx] + 1
                q.append((df, dy, dx))
    return -1


def escape(floor_cnt, Y, X):
    building = []
    start = []

    for f in range(floor_cnt):
        floor = []
        for y in range(Y):
            floor.append(sys.stdin.readline().rstrip())
            for x in range(X):
                if floor[y][x] == 'S':
                    start = [f, y, x]
        building.append(floor)
        empty = sys.stdin.readline().rstrip()
    res = BFS(building, start, floor_cnt, Y, X)
    if res >= 0:
        print(f'Escaped in {res} minute(s).')
    else:
        print('Trapped!')

while True:
    L, C, S = map(int, sys.stdin.readline().split())
    if not (L+C+S):
        break
    escape(L, C, S)