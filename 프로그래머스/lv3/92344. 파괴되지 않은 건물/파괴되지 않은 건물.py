def solution(board, skill):
    answer = 0
    y_length = len(board)
    x_length = len(board[0])
    prefix = [[0]*(x_length+1) for _ in range(y_length+1)]
    for type, r1, c1, r2, c2, degree in skill:
        prefix[r1][c1] += degree if type == 2 else -degree
        prefix[r1][c2+1] += -degree if type == 2 else degree
        prefix[r2+1][c1] += -degree if type == 2 else degree
        prefix[r2+1][c2+1] += degree if type == 2 else -degree

    for y in range(y_length):
        for x in range(x_length):
            prefix[y][x + 1] += prefix[y][x]

    # 열 기준 누적합
    for x in range(x_length):
        for y in range(y_length):
            prefix[y + 1][x] += prefix[y][x]

    for y in range(y_length):
        for x in range(x_length):
            board[y][x] += prefix[y][x]
            if board[y][x] > 0:
                answer += 1
    return answer