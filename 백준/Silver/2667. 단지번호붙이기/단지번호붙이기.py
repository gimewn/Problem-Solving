import sys
from collections import deque

def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    count = 1

    while q:
        ny, nx = q.popleft()

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dy, dx = ny+i, nx+j
            if 0 <= dy < N and 0 <= dx < N and board[dy][dx] == '1' and not check[dy][dx]:
                check[dy][dx] = 1
                count += 1
                q.append((dy, dx))

    return count

N = int(input())

board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
check = [[0]*N for _ in range(N)]
complex = []

for y in range(N):
    for x in range(N):
        if board[y][x] == '1' and not check[y][x]:
            check[y][x] = 1
            complex.append(bfs(y, x))

complex.sort()

print(len(complex))
for count in complex:
    print(count)