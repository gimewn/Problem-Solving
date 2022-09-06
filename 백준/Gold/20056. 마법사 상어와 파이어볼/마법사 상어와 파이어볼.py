import sys
input = sys.stdin.readline

dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def cal(y, x):
    length = len(board[y][x])
    tempM = 0
    tempS = 0
    tempOdd = 0 # 방향이 홀수일 때
    tempEven = 0 # 방향이 짝수일 때
    for m, s, d in board[y][x]:
        tempM += m # 질량 더하기
        tempS += s # 속력 더하기
        if d % 2: # 방향이 짝수인지 홀수인지 구분
            tempOdd += 1
        else:
            tempEven += 1

    tempM //= 5
    tempS //= length

    if tempOdd == length or tempEven == length: # 방향이 모두 짝수이거나 모두 홀수이거나
        changeDir = [0, 2, 4, 6]
    else:
        changeDir = [1, 3, 5, 7]

    if tempM: # 질량이 0인 파이어볼은 소멸이므로
        for cd in changeDir: # 방향 순으로
            fireball.append([y, x, tempM, tempS, cd]) # 파이어볼 추가
    board[y][x] = [] # 원래 칸 초기화

def moveFireball(fb):
    y, x, m, s, d = fb
    my = (y+dir[d][0]*s)%N # y 이동, 처음과 끝 연결
    mx = (x + dir[d][1] * s) % N # x 이동, 처음과 끝 연결
    board[my][mx].append([m, s, d]) # 칸에 삽입

N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
fireball = []
res = 0

for _ in range(M):
    y, x, m, s, d = map(int, input().split()) # y, x, 질량, 속력, 방향
    fireball.append([y-1, x-1, m, s, d])

for _ in range(K):
    # 파이어볼 이동
    while fireball:
        fb = fireball.pop(0)
        moveFireball(fb)
    # 이동이 끝난 후
    for y in range(N):
        for x in range(N):
            if len(board[y][x]) >= 2:
                cal(y, x)
            elif len(board[y][x]) == 1:
                m, s, d = board[y][x][0]
                fireball.append([y, x, m, s, d])
                board[y][x] = []

for fb in fireball:
    res += fb[2]

print(res)