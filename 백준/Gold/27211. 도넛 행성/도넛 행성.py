import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

donut = [list(map(int, input().split())) for _ in range(N)]

visit = [[0]*M for _ in range(N)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = 0

def BFS(starty, startx):

    q = deque()
    q.append((starty, startx))

    while q:
        ny, nx = q.popleft()
        for i, j in dir:
            dy = ny+i
            dx = nx+j
            if dy < 0:
                dy += N
            elif dy >= N:
                dy -= N
            if dx < 0:
                dx += M
            elif dx >= M:
                dx -= M
            if not visit[dy][dx] and not donut[dy][dx]:
                visit[dy][dx] = 1
                q.append((dy, dx))

for y in range(N):
    for x in range(M):
        if not donut[y][x] and not visit[y][x]:
            answer += 1
            visit[y][x] = 1
            BFS(y, x)

print(answer)