import sys

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def BFS():
    q = set()
    q.add((0, 0, board[0][0]))
    max_cnt = 1

    while q:
        ny, nx, nlist = q.pop()
        max_cnt = max(max_cnt, len(nlist))

        for i, j in dir:
            dy, dx = ny+i, nx+j
            if 0 <= dy < R and 0 <= dx < C and board[dy][dx] not in nlist:
                q.add((dy, dx, nlist+board[dy][dx]))

    return max_cnt

R, C = map(int, sys.stdin.readline().split())

board = [sys.stdin.readline().rstrip() for _ in range(R)]

print(BFS())