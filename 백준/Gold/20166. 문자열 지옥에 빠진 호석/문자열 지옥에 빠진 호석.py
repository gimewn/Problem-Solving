import sys
from collections import deque

def bfs(sy, sx):
    q = deque()
    q.append((sy, sx, board[sy][sx]))

    while q:
        ny, nx, nword = q.popleft()

        if nword in likes:
            likes[nword] += 1

        if len(nword) >= 5:
            continue

        for i, j in (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1):
            dy, dx = (ny + i) % N, (nx + j) % M
            q.append((dy, dx, nword + board[dy][dx]))


inputs = sys.stdin.readline

N, M, K = map(int, inputs().split())

board = [list(inputs().rstrip()) for _ in range(N)]
check = [[0]*M for _ in range(N)]

likes = {}

for _ in range(K):
    word = inputs().rstrip()
    likes[word] = 0

for y in range(N):
    for x in range(M):
        bfs(y, x)

for value in likes.values():
    print(value)