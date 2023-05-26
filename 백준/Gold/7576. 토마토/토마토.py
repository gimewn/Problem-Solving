import sys
from collections import deque

X, Y = map(int, input().split())

tomato = [[0]*X for _ in range(Y)]
cnt = Y*X
ripen = deque()


for y in range(Y):
    temp = list(map(int, input().split()))
    for x in range(X):
        if temp[x] == -1:
            cnt -= 1
            tomato[y][x] = -1
        elif temp[x] == 1:
            cnt -= 1
            ripen.append((y, x, 0))
            tomato[y][x] = 1

def BFS(q, cnt):
    while q:
        ny, nx, day = q.popleft()

        for i, j in (-1, 0), (1, 0), (0, 1), (0, -1):
            dy, dx = ny + i, nx + j
            if 0 <= dy < Y and 0 <= dx < X and not tomato[dy][dx]:
                tomato[dy][dx] = 1
                cnt -= 1
                ripen.append((dy, dx, day + 1))

            if cnt == 0:
                return day + 1

    return -1

if not cnt:
    print(cnt)
else:
    print(BFS(ripen, cnt))