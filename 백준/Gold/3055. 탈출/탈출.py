import sys
from collections import deque

dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def water_bfs(q):
    while q:
        ny, nx = q.popleft()
        for i, j in dir:
            dy, dx = ny+i, nx+j
            if 0 <= dy < R and 0 <= dx < C:
                # 돌이 없고, 비버의 집이 아니며, 물이 아직 안 차오른 곳이면
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
        # 위치가 비버의 집이면 방문한 시간 return
        if ny == e[0] and nx == e[1]:
            return ncnt
        for i, j in dir:
            dy, dx = ny+i, nx+j
            if 0 <= dy < R and 0 <= dx < C:
                # 방문한 적 없고, 돌이 없으며, 물이 아직 안 차올랐거나 차오를 일 없으면
                if not visit[dy][dx] and board[dy][dx] != 'X' and (water[dy][dx] > ncnt+1 or water[dy][dx] == -1):
                    visit[dy][dx] = 1
                    q.append((dy, dx, ncnt+1))
    return -1


R, C = map(int, sys.stdin.readline().split())

board = []

# 고슴도치 위치
start = 0, 0
# 비버 위치
end = 0, 0
# 물 초기 위치
water_position = deque()
# 물이 차오를 시기 기록
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