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
            # 수색 범위 내에 있으면 아이템 줍기
            if board[j][k] <= M:
                cal_itemes[j][k] = items[k]

for idx in range(1, N+1):
    answer = max(answer, sum(cal_itemes[idx]))

print(answer)