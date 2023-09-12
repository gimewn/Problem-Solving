import sys

def check_able(row, made):
    for idx in range(1, N):
        diff = row[idx] - row[idx-1]
        if abs(diff) > 1:
            return False

        if row[idx] < row[idx-1]:
            for l in range(L):
                if idx + l >= N or made[idx+l] or row[idx] != row[idx+l]:
                    return False
                if row[idx] == row[idx+l]:
                    made[idx+l] = 1
        elif row[idx] > row[idx-1]:
            for l in range(L):
                if idx - l - 1 < 0 or row[idx-1] != row[idx-l-1] or made[idx-l-1]:
                    return False
                if row[idx] == row[idx-l-1]:
                    made[idx-l-1] = 1
    return True

N, L = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = 0

for row in board:
    made = [0]*N
    if check_able(row, made):
        answer += 1

for y in range(N):
    made = [0]*N
    row = [0]*N
    for x in range(N):
        row[x] = board[x][y]
    if check_able(row, made):
        answer += 1

print(answer)