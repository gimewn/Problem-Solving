import sys

def increase_same_row(row):
    global answer
    if row not in same_row:
        same_row[row] = 0
    same_row[row] += 1
    answer = max(answer, same_row[row])

N, M = map(int, sys.stdin.readline().split())

board = [sys.stdin.readline().rstrip() for _ in range(N)]

K = int(sys.stdin.readline())

answer = 0

same_row = {}

for x in range(N):
    zero = 0
    for lamp in board[x]:
        if lamp == '0':
            zero += 1
    if zero <= K:
        if K % 2 and zero % 2:
            increase_same_row(board[x])
        elif not K % 2 and not zero % 2:
            increase_same_row(board[x])

print(answer)