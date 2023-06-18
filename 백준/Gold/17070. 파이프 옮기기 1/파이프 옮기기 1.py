import sys

N = int(sys.stdin.readline())

board = [list(sys.stdin.readline().split()) for _ in range(N)]

check = [[[0]*3 for _ in range(N)] for _ in range(N)]

answer = 0

# (0, 1) => 가로 연결되어 있음
check[0][1][0] = 1

for y in range(N):
    # 0, 0이 가로 => 0열은 쓰일 일이 없음
    for x in range(1, N):
        if board[y][x] == '1':
            continue
        # 대각선 체크용 flag
        flag = 1

        # 옆(0) 체크
        if x-1 >= 1 and board[y][x-1] != '1':
            if check[y][x-1][0] or check[y][x-1][2]:
                # (y, x-1)이 가로거나 대각선 => 가로 그을 수 있음
                check[y][x][0] += check[y][x-1][0] + check[y][x-1][2]
        else:
            # 옆이 벽이면 대각선 불가능
            flag = 0

        # 위(1) 체크
        if y-1 >= 0 and board[y-1][x] != '1':
            if check[y-1][x][1] or check[y-1][x][2]:
                # (y-1, x)가 세로거나 대각선 => 세로 그을 수 있음
                check[y][x][1] += check[y-1][x][1] + check[y-1][x][2]
        else:
            # 위가 벽이면 대각선 불가능
            flag = 0

        # 대각선(2) 체크
        # 옆과 위가 벽이 아니고, 범위 내이며, 좌측 대각선이 연결된 파이프가 있으면 대각선 그을 수 있음
        if flag and y-1 >= 0 and x-1 >= 1 and sum(check[y-1][x-1]):
            check[y][x][2] += sum(check[y-1][x-1])

print(sum(check[-1][-1]))