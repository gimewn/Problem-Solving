from collections import deque

N, T = map(int, input().split(" "))

road = [[] for _ in range(N)]

dir = {'U' : (-1, 0), 'D' : (1, 0), 'L' : (0, -1), 'R': (0, 1)}

# 신호별 갈 수 있는 방향
signal = [0, ['R', 'U', 'R', 'D'], ['U', 'L', 'U', 'R'], ['L', 'U', 'L', 'D'], ['D', 'L', 'D', 'R'],
          ['R', 'U', 'R'], ['U', 'L', 'U'], ['L', 'L', 'D'], ['D', 'D', 'R'],
          ['R', 'R', 'D'], ['U', 'U', 'R'], ['L', 'U', 'L'], ['D', 'L', 'D']]

for idx in range(N):
    temp = []
    for _ in range(N):
        temp.append(list(map(int, input().split())))
    road[idx] = temp

answer = set()

def BFS():
    q = deque()
    # 좌표, 방향, 시간
    q.append(((0, 0), 'U', 0))

    while q:
        now, prev_dir, time = q.popleft()
        # set에 좌표 추가
        answer.add(now)
        # 현재 신호
        now_signal = road[now[0]][now[1]][time % 4]
        # 갈 수 있는 방향
        move = signal[now_signal]
        # 만약 줄기가 전 방향과 일치하지 않다면 올 수 없던 것이므로 continue
        if prev_dir != move[0]:
            continue
        # 갈 수 있는 방향 하나씩 체크
        for d in move[1:]:
            dy, dx = now[0]+dir[d][0], now[1]+dir[d][1]
            # 범위 내이고, 시간이 T보다 적다면
            if 0 <= dy < N and 0 <= dx < N and time < T:
                # q에 추가
                q.append(((dy, dx), d, time+1))

BFS()

print(len(answer))