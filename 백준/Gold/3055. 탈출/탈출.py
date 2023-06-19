import sys
from collections import deque

dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def water_bfs(q):
    while q:
        ny, nx = q.popleft()
        for i, j in dir:
            dy, dx = ny+i, nx+j
            if 0 <= dy < R and 0 <= dx < C:
                if board[dy][dx] != 'X' and board[dy][dx] != 'D' and water[dy][dx] < 0:
                    water[dy][dx] = water[ny][nx] + 1
                    q.append((dy, dx))
def escape_bfs(s, e):
    q = deque()
    q.append((s[0], s[1], 0))
    visit = [[0]*C for _ in range(R)]
    visit[s[0]][s[1]] = 1
    while q:
        ny, nx, ncnt = q.popleft()
        if ny == e[0] and nx == e[1]:
            return ncnt
        for i, j in dir:
            dy, dx = ny+i, nx+j
            if 0 <= dy < R and 0 <= dx < C:
                if not visit[dy][dx] and board[dy][dx] != 'X' and (water[dy][dx] > ncnt+1 or water[dy][dx] == -1):
                    visit[dy][dx] = 1
                    q.append((dy, dx, ncnt+1))
    return -1


R, C = map(int, sys.stdin.readline().split())

board = []

start = 0, 0
end = 0, 0
water_position = deque()
water = [[-1]*C for _ in range(R)]

for y in range(R):
    lst = list(sys.stdin.readline().rstrip())
    for x in range(C):
        if lst[x] == 'D':
            end = y, x
        elif lst[x] == 'S':
            start = y, x
        elif lst[x] == '*':
            water[y][x] = 0
            water_position.append((y, x))
    board.append(lst)

water_bfs(water_position)
answer = escape_bfs(start, end)

if answer < 0:
    print("KAKTUS")
else:
    print(answer)