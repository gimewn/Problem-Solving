import sys

input = sys.stdin.readline

N = int(input())

student = {}

for _ in range(N**2):
    like_list = list(map(int, input().split()))
    student[like_list[0]] = set(like_list[1:])

answer = 0

board = [[0]*N for _ in range(N)]
check = [[0]*N for _ in range(N)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def check_empty(y, x):
    global max_empty
    empty = 0
    for i, j in dir:
        dy, dx = y+i, x+j
        if 0 <= dy < N and 0 <= dx < N:
            if board[dy][dx] == 0:
                empty += 1
    if empty >= max_empty:
        if empty > max_empty:
            max_empty_set.clear()
            max_empty = empty
        max_empty_set.add((y, x))

def check_like(y, x, snum):
    global max_like
    like = 0
    for i, j in dir:
        dy, dx = y+i, x+j
        if 0 <= dy < N and 0 <= dx < N:
            if board[dy][dx] != 0:
                if board[dy][dx] in student[snum]:
                    like += 1
    if like >= max_like:
        if like > max_like:
            max_like_set.clear()
            max_like = like
        max_like_set.add((y, x))

def count_like(y, x):
    like = 0
    s = board[y][x]
    for i, j in dir:
        dy, dx = y + i, x + j
        if 0 <= dy < N and 0 <= dx < N:
            if board[dy][dx] in student[s]:
                like += 1
    return like

for s in student:
    max_like, max_empty = 0, 0
    max_like_set, max_empty_set = set(), set()
    for y in range(N):
        for x in range(N):
            # 아직 아무도 앉지 않았다면
            if board[y][x] == 0:
                # 인접한 자리의 좋아하는 사람 수 카운트
                check_like(y, x, s)
    # 인접한 좋아하는 사람 가장 많은 자리가 여러 개라면
    if len(max_like_set) > 1:
        # 그 자리 중 인접한 빈 칸 가장 많은 자리 카운트
        for y, x in max_like_set:
            check_empty(y, x)
        # 인접한 빈 칸 가장 많은 자리가 여러 개라면
        if len(max_empty_set) > 1:
            my, mx = N, N
            # 행, 열 번호 비교
            for y, x in max_empty_set:
                # y가 더 작다면
                if y < my:
                    # my, mx 교체
                    my, mx = y, x
                # y가 같다면
                elif y == my:
                    # x 비교 -> 더 작을 경우 교체
                    if mx < x:
                        mx = x
            board[my][mx] = s
        else:
            # 인접한 빈 칸 가장 많은 자리가 1개라면 앉히기
            ey, ex = max_empty_set.pop()
            board[ey][ex] = s
    else:
        # 인접한 좋아하는 사람 가장 많은 자리가 1개라면 앉히기
        ly, lx = max_like_set.pop()
        board[ly][lx] = s

for y in range(N):
    for x in range(N):
        like_student = count_like(y, x)
        if like_student:
            answer += 10**(like_student-1)

print(answer)
