def check(index, d):

    if index - 1 >= 0 and not check_rot[index-1] and board[index - 1][2] != board[index][6]:
        check_rot[index - 1] = d * -1
        check(index-1, d*-1)
    if index + 1 < 4 and not check_rot[index+1] and board[index + 1][6] != board[index][2]:
        check_rot[index + 1] = d * -1
        check(index+1, d*-1)


board = [list(map(int, list(input()))) for _ in range(4)]

k = int(input())

answer = 0

for _ in range(k):
    num, direction = map(int, input().split())
    check_rot = [0] * 4
    check_rot[num-1] = direction
    check(num-1, direction)
    for idx in range(4):
        if check_rot[idx] != 0:
            if check_rot[idx] == 1:
                board[idx] = [board[idx][-1]]+board[idx][:-1]
            elif check_rot[idx] == -1:
                board[idx] = board[idx][1:]+[board[idx][0]]

for idx in range(4):
    if board[idx][0] == 1:
        answer += 2**idx

print(answer)