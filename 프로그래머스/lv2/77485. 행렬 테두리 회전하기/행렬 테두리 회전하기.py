def solution(rows, columns, queries):
    answer = []
    board = [[0]*(columns+1) for _ in range(rows+1)]
    num = 1
    for x in range(1, rows+1):
        for y in range(1, columns+1):
            board[x][y] = num
            num += 1

    for idx in range(len(queries)):
        x1, y1, x2, y2 = queries[idx]
        start = board[x1][y1]
        minNum = start

        # y1열 고정, ↑
        for x in range(x1+1, x2+1):
            board[x-1][y1] = board[x][y1]
            minNum = min(minNum, board[x][y1])

        # x2행 고정, ←
        for y in range(y1+1, y2+1):
            board[x2][y-1] = board[x2][y]
            minNum = min(minNum, board[x2][y])

        # y2열 고정, ↓
        for x in range(x2-1, x1-1, -1):
            board[x+1][y2] = board[x][y2]
            minNum = min(minNum, board[x][y2])

        # x1행 고정, →
        for y in range(y2-1, y1, -1):
            board[x1][y+1] = board[x1][y]
            minNum = min(minNum, board[x1][y])

        board[x1][y1+1] = start
        
        answer.append(minNum)

    return answer