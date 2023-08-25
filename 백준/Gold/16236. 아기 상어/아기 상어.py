import sys
from collections import deque

def BFS(X, Y, size):
    q = deque([(X, Y, 0)])
    check = [[0]*N for _ in range(N)]
    check[X][Y] = 1
    can_eat = []

    while q:
        nx, ny, ntime = q.popleft()
        # board[nx][ny]가 0이 아니고, 상어보다 작은 물고기가 있다면 먹을 수 있음
        if board[nx][ny] and board[nx][ny] < size:
            can_eat.append((nx, ny, ntime))
        for i, j in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            dx, dy = nx+i, ny+j
            # 범위 벗어나면 continue
            if 0 > dx or dx >= N or 0 > dy or dy >= N:
                continue
            # 상어보다 큰 물고기 있으면 지나갈 수 없으므로 continue
            if board[dx][dy] > size:
                continue
            # 방문한 적 있으면 continue
            if check[dx][dy]:
                continue
            check[dx][dy] = 1
            q.append((dx, dy, ntime + 1))
    # can_eat에 아무것도 없으면 엄마 상어에게 도움 요청해야 함
    if not can_eat:
        return False
    # 거리, 제일 위에 있는, 제일 왼쪽에 있는 순으로 정렬
    can_eat.sort(key=lambda x: (x[2], x[0], x[1]))
    return can_eat[0]

N = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

sx, sy = 0, 0

for x in range(N):
    for y in range(N):
        # 상어 초기 위치
        if board[x][y] == 9:
            sx, sy = x, y
            board[x][y] = 0

shark = 2
eat = 0
time = 0

while True:
    res = BFS(sx, sy, shark)
    # 먹을 수 있는 물고기가 없음 => 엄마 상어에게 도움 요청 (break)
    if not res:
        break
    newx, newy, count = res
    # 상어 위치 갱신
    sx, sy = newx, newy
    # 물고기 먹음 기록
    board[newx][newy] = 0
    eat += 1
    # 먹은 물고기 수 == 상어 크기 => 상어 크기 1 증가
    if eat == shark:
        shark += 1
        eat = 0
    time += count

print(time)