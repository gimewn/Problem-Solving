import sys

def dfs(ny, nx):
    global answer

    if ny == 0 and nx == C-1 and visit[ny][nx] == K:
        answer += 1
        return

    if visit[ny][nx] >= K:
        return

    for i, j in (-1, 0), (1, 0), (0, -1), (0, 1):
        dy, dx = ny+i, nx+j
        if 0 <= dy < R and 0 <= dx < C and not visit[dy][dx] and board[dy][dx] != 'T':
            visit[dy][dx] = visit[ny][nx] + 1
            dfs(dy, dx)
            visit[dy][dx] = 0

inputs = sys.stdin.readline

R, C, K = map(int, inputs().split())

board = [list(inputs().rstrip()) for _ in range(R)]

answer = 0

visit = [[0]*C for _ in range(R)]

visit[R-1][0] = 1

dfs(R-1, 0)

print(answer)