import sys
from collections import deque

dir = [(0, -1), (0, 1), (1, 0), (-1, 0)]

def bfs(sy, sx):
    q = deque()
    # 벽 안 뚫음 / 벽 뚫음
    visit = [[[0]*2 for _ in range(M)] for _ in range(N)]
    # 첫 번째 => 벽 안 뚫음
    q.append((sy, sx, 0))
    visit[sy][sx][0] = 1

    while q:
        ny, nx, nb = q.popleft()
        if ny == N-1 and nx == M-1:
            return visit[ny][nx][nb]

        for i, j in dir:
            dy, dx = ny+i, nx+j
            if 0 <= dy < N and 0 <= dx < M:
                # 벽인 경우 => 한 번이라도 뚫었으면 nb는 1
                # nb가 1일 때만 => 벽을 한 번도 안 뚫었을 때만 진입
                if board[dy][dx] == '1' and not nb:
                    visit[dy][dx][1] = visit[ny][nx][nb] + 1
                    q.append((dy, dx, 1))
                # 벽이 아닌 경우 => 방문한 적 없으면 진입
                elif board[dy][dx] == '0' and not visit[dy][dx][nb]:
                    visit[dy][dx][nb] = visit[ny][nx][nb] + 1
                    q.append((dy, dx, nb))
    return -1

N, M = map(int, input().split())

board = [list(sys.stdin.readline()) for _ in range(N)]
check = [[0]*M for _ in range(N)]
answer = 2e9

print(bfs(0, 0))