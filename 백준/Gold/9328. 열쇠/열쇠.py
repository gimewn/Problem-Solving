import sys
from collections import deque

input = sys.stdin.readline
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def unlock():
    global door
    if sum(door):
        for y in range(Y+2):
            for x in range(X+2):
                if board[y][x].isupper():
                    if door[ord(board[y][x])-ord('A')]:
                        board[y][x] = '.'
        door = [0]*26
def BFS():
    global doc
    q = deque()
    q.append((0, 0))
    visit = [[0]*(X+2) for _ in range(Y+2)]
    visit[0][0] = 1
    while q:
        ny, nx = q.popleft()
        for i, j in dir:
            dy, dx = ny+i, nx+j
            if 0 <= dy < Y+2 and 0 <= dx < X+2:
                if visit[dy][dx] == 1: continue
                if board[dy][dx] == '*': continue
                elif board[dy][dx].isupper():continue
                elif board[dy][dx] == '$': # 문서면 줍기
                    doc += 1
                elif board[dy][dx].islower(): # 키 발견 시
                    door[ord(board[dy][dx])-ord('a')] = 1 # 문 리스트에 표시
                board[dy][dx] = '.'
                visit[dy][dx] = 1
                q.append((dy, dx))

T = int(input())

for tc in range(T):
    Y, X = map(int, input().split())
    board = [[] for _ in range(Y+2)]
    board[0] = board[Y+1] = ['.']*(X+2)
    door = [0]*26
    doc = 0 # 훔친 문서 갯수
    for idx in range(1, Y+1): # 새로운 맵
        temp_lst = list(input())
        temp_lst.pop() # sys => 처리
        board[idx] = ['.'] + temp_lst + ['.']
    temp = list(input())
    temp.pop() # sys => 처리
    for k in temp:
        if k != '0':
            door[ord(k)-ord('a')] = 1 # 문에 열쇠 있다고 표시
    for y in range(Y+2):
        for x in range(X+2):
            if ord(board[y][x]) >= ord('A') and ord(board[y][x]) <= ord('Z'): # 방이면
                if door[ord(board[y][x])-ord('A')]: # 보유 중인 열쇠로 열리면 열기
                    board[y][x] = '.'
    while True:
        unlock()
        BFS()
        if sum(door) == 0:
            break
    print(doc)