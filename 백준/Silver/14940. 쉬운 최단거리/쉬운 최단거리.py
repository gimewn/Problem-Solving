import sys
from collections import deque

Y, X = map(int, input().split())

board = [0]*Y
visit = [[0]*X for _ in range(Y)]
res = [[-1]*X for _ in range(Y)]
q = deque()

for idx in range(Y):
    temp = list(map(int, sys.stdin.readline().split()))
    for x in range(X):
        if temp[x] == 2:
            q.append((idx, x, 0))
            visit[idx][x] = 1
            res[idx][x] = 0
        elif temp[x] == 0:
            visit[idx][x] = 1
            res[idx][x] = 0

    board[idx] = temp

while q:
    ny, nx, cnt = q.popleft()

    for i, j in (-1, 0), (1, 0), (0, 1), (0, -1):
        dy, dx = ny+i, nx+j
        if 0 <= dy < Y and 0 <= dx < X and not visit[dy][dx] and board[dy][dx] == 1:
            visit[dy][dx] = 1
            res[dy][dx] = cnt+1
            q.append((dy, dx, cnt+1))

for r in res:
    print(*r)