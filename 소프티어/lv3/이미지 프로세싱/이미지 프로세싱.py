from collections import deque

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(y, x, change_color, now_color):
    # 중복체크
    visit = [[0]*X for _ in range(Y)]
    q = deque()
    q.append((y, x))
    visit[y][x] = 1
    # 색 바꿔줄 좌표
    change = [(y, x)]

    while q:
        ny, nx = q.popleft()
        # 4방향으로 확인
        for i, j in dir:
            dy, dx = ny+i, nx+j
            # 범위 내에 있으면서, 방문하지 않았고, 색이 같다면
            if 0 <= dy < Y and 0 <= dx < X and visit[dy][dx] == 0 and board[dy][dx] == now_color:
                # 방문 체크
                visit[dy][dx] = 1
                # 색 바꿔줄 좌표로 추가
                change.append((dy, dx))
                # q에 추가
                q.append((dy, dx))
    # 색 바꿔주기
    for cy, cx in change:
        board[cy][cx] = change_color


Y, X = map(int, input().split(" "))

board = [list(input().split(" ")) for _ in range(Y)]

cnt = int(input())

for _ in range(cnt):
    i, j, c = map(int, input().split(" "))
    BFS(i-1, j-1, str(c), board[i-1][j-1])


for b in board:
    print(' '.join(b))