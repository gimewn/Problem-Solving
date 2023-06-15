import sys

N, M, R = map(int, sys.stdin.readline().split())

items = [0] + list(map(int, sys.stdin.readline().split()))
board = [[2e9]*(N+1) for _ in range(N+1)]
answer = 0
cal_itemes = [[0]*(N+1) for _ in range(N+1)]

# 자기자신 초기화
for i in range(1, N+1):
    board[i][i] = 0

for _ in range(R):
    a, b, length = map(int, sys.stdin.readline().split())

    board[a][b] = min(board[a][b], length)
    board[b][a] = board[a][b]

# 최단거리 갱신
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            board[j][k] = min(board[j][k], board[j][i] + board[i][k])

for y in range(1, N+1):
    temp = 0
    for x in range(1, N+1):
        if board[y][x] <= M:
            temp += items[x]
    answer = max(answer, temp)

print(answer)