import sys
from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    count = 1
    while q:
        nx, ny = q.popleft()
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dx, dy = nx+i, ny+j
            if 0 > dx or dx >= X or 0 > dy or dy >= Y:
                continue
            if check[dx][dy]:
                continue
            if board[dx][dy] == board[x][y]:
                check[dx][dy] = 1
                count += 1
                q.append((dx, dy))
    return count

Y, X = map(int, input().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(X)]
check = [[0]*Y for _ in range(X)]
W, B = 0, 0

for x in range(X):
    for y in range(Y):
        if not check[x][y]:
            check[x][y] = 1
            thisCount = bfs(x, y)
            if board[x][y] == 'W':
                W += thisCount ** 2
            else:
                B += thisCount ** 2

print(W, B)