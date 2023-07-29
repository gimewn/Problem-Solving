import sys
from collections import deque

def check_dir(x, y):
    count = 0
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dx, dy = x+i, y+j
        if 0 > dx or dx >= X or 0 > dy or dy >= Y:
            continue
        if not board[dx][dy]:
            count += 1
    return count

def find_ice():
    newQ = deque()
    for x in range(X):
        for y in range(Y):
            if board[x][y]:
                # 빙산이면 q에 담기
                newQ.append((x, y))
    return newQ, len(newQ)

def melt_ice(q):
    melt = deque()
    while q:
        nx, ny = q.popleft()
        count = check_dir(nx, ny)
        melt.append((nx, ny, count))

    for mx, my, mCount in melt:
        board[mx][my] -= mCount
        if board[mx][my] < 0:
            board[mx][my] = 0

def bfs_ice(x, y):

    q = deque([(x, y)])
    count = set([(x, y)])

    while q:
        nx, ny = q.popleft()

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dx, dy = nx+i, ny+j
            if 0 > dx or dx >= X or 0 > dy or dy >= Y:
                continue
            if board[dx][dy] and (dx, dy) not in count:
                q.append((dx, dy))
                count.add((dx, dy))
    return len(count)

X, Y = map(int, input().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(X)]
turn = 0

q, ice = find_ice()

while True:
    turn += 1
    melt_ice(q)
    q, ice = find_ice()
    if q:
        bfs_count = bfs_ice(q[0][0], q[0][1])
    else:
        break

    if bfs_count != ice:
        print(turn)
        exit(0)

print(0)