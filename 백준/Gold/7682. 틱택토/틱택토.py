import sys

input = sys.stdin.readline

while True:
    temp = input().rstrip()
    if temp == 'end':
        break
    board = [[0]*3 for _ in range(3)]
    y, x = 0, 0
    x_cnt, o_cnt = 0, 0
    for t in temp:
        if t == 'X':
            x_cnt += 1
        elif t == 'O':
            o_cnt += 1
        board[y][x] = t
        x += 1
        if x > 2:
            y += 1
            x = 0
    # X가 O보다 1개 더 많거나 같을 경우만 valid가 나올 수 있음
    if x_cnt - o_cnt == 1 or x_cnt == o_cnt:
        # X와 O의 이긴 횟수 세기
        win_cnt = {'X': 0, 'O': 0}
        # X와 O의 가로, 세로, 대각선 검사 =>
        for i in range(3):
            # 가로 검사
            if board[i][0] == board[i][1] == board[i][2] == 'X':
                win_cnt['X'] += 1
            elif board[i][0] == board[i][1] == board[i][2] == 'O':
                win_cnt['O'] += 1
            # 세로 검사
            if board[0][i] == board[1][i] == board[2][i] == 'X':
                win_cnt['X'] += 1
            elif board[0][i] == board[1][i] == board[2][i] == 'O':
                win_cnt['O'] += 1
        # 대각선 검사
        if board[0][0] == board[1][1] == board[2][2] == 'X':
            win_cnt['X'] += 1
        elif board[0][0] == board[1][1] == board[2][2] == 'O':
            win_cnt['O'] += 1
        if board[0][2] == board[1][1] == board[2][0] == 'X':
            win_cnt['X'] += 1
        elif board[0][2] == board[1][1] == board[2][0] == 'O':
            win_cnt['O'] += 1

        flag = False
        # O가 승리했고 X가 승리하지 않았을 경우 => X와 O의 개수가 동일해야 함
        if win_cnt['O'] and not win_cnt['X'] and x_cnt == o_cnt:
            flag = True
        # X가 승리했고 O가 승리하지 않았을 경우 => X가 O보다 1개 더 많아야 함
        elif win_cnt['X'] and not win_cnt['O'] and x_cnt > o_cnt:
            flag = True
        # 둘 다 승리하지 않았을 경우 => X가 O보다 1개 더 많아야 하고, 보드가 꽉 찬 상태여야 하므로 둘의 합이 9여야 함
        elif not win_cnt['X'] and not win_cnt['O'] and x_cnt > o_cnt and x_cnt + o_cnt == 9:
            flag = True

        if flag:
            print('valid')
        else:
            print('invalid')
    else:
        print('invalid')