import sys
from collections import deque

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def main():

    def bfs(starty, startx):
        q = deque()
        q.append((starty, startx))
        visit[starty][startx] = 1
        while q:
            ny, nx = q.popleft()
            for i, j in dir:
                dy, dx = ny+i, nx+j
                if 1 <= dy <= N and 1 <= dx <= M and visit[dy][dx] == 2:
                    visit[dy][dx] = 1
                    visit[starty][startx] += 1
                    q.append((dy, dx))

        return visit[starty][startx]

    N, M, K = map(int, sys.stdin.readline().split())

    trash = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
    visit = [[0]*(M+1) for _ in range(N+1)]

    answer = 0

    for y, x in trash:
        visit[y][x] = 2

    for y, x in trash:
        if visit[y][x] == 2:
            answer = max(answer, bfs(y, x))

    print(answer)


if __name__ == '__main__':
    main()