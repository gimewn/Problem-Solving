import sys
from collections import deque

def BFS(X, Y, size):
    q = deque([(X, Y, 0)])
    check = [[0]*N for _ in range(N)]
    check[X][Y] = 1
    can_eat = []

    while q:
        nx, ny, ntime = q.popleft()
        if board[nx][ny] and board[nx][ny] < size:
            can_eat.append((nx, ny, ntime))
        for i, j in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            dx, dy = nx+i, ny+j
            if 0 > dx or dx >= N or 0 > dy or dy >= N:
                continue
            if board[dx][dy] > size:
                continue
            if check[dx][dy]:
                continue
            check[dx][dy] = 1
            q.append((dx, dy, ntime + 1))

    if not can_eat:
        return False
    can_eat.sort(key=lambda x: (x[2], x[0], x[1]))
    return can_eat[0]

N = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

sx, sy = 0, 0

for x in range(N):
    for y in range(N):
        if board[x][y] == 9:
            sx, sy = x, y
            board[x][y] = 0

shark = 2
eat = 0

time = 0

while True:
    res = BFS(sx, sy, shark)
    if not res:
        break
    newx, newy, count = res
    sx, sy = newx, newy
    board[newx][newy] = 0
    eat += 1
    if eat == shark:
        shark += 1
        eat = 0
    time += count

print(time)