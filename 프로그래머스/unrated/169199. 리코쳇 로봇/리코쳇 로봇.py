from collections import deque


def solution(board):
    answer = 0
    # 상하좌우
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    Y = len(board)
    X = len(board[0])
    sy, sx = 0, 0

    # 첫 시작 좌표 구하기
    for y in range(Y):
        for x in range(X):
            if board[y][x] == "R":
                sy, sx = y, x

    def BFS(y, x):
        cnt = 0
        q = deque()
        q.append((y, x, 0))
        check = [[0]*X for _ in range(Y)]
        check[y][x] = 1

        while q:
            ny, nx, cnt = q.popleft()

            if board[ny][nx] == "G":
                return cnt

            for i, j in dir:
                plus = 1
                while True:
                    dy, dx = ny + i * plus, nx + j * plus
                    py, px = ny + i * (plus - 1), nx + j * (plus - 1)
                    if dy == -1 or dy == Y or dx == -1 or dx == X or (dy >= 0 and dy < Y and dx >= 0 and dx < X and board[dy][dx] == "D"):
                        if check[py][px] == 0 and board[py][px] != "D":
                            check[py][px] = 1
                            q.append((py, px, cnt + 1))
                        break
                    if dy > Y or dy < 0 or dx > X or dx < 0:
                        break
                    plus += 1

        return -1

    answer = BFS(sy, sx)

    return answer