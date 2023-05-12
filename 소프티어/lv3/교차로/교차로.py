import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

answer = [-1]*n

road = {'A': deque(), 'B': deque(), 'C': deque(), 'D': deque()}

# 각 도로의 오른쪽 도로
right = {'A': 'D', 'B': 'A', 'C': 'B', 'D': 'C'}

start_time = sys.maxsize

for idx in range(n):
    t, w = input().split()
    road[w].append((int(t), idx))
    # 가장 빠른 출발 시간 갱신
    start_time = min(start_time, int(t))

# 가장 빠른 시간부터 시작
now = start_time

while road['A'] or road['B'] or road['C'] or road['D']:
    min_time = sys.maxsize
    pop = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

    for alp in road:
        # 만약 도로에 차가 있다면
        if road[alp]:
            # 첫 번째 차들의 가장 빠른 출발 시간 갱신
            min_time = min(min_time, road[alp][0][0])
            # 현재 시간에 진입가능한 차가 있다면 진입
            if road[alp][0][0] <= now:
                pop[alp] = 1

    # A, B, C, D 모두 차가 진입해 있다면
    # 교착 상태
    if pop['A'] + pop['B'] + pop['C'] + pop['D'] == 4:
        break

    # 어떤 차도 진입해있지 않다면
    # 각 도로의 첫 번째 차들의 출발 시간 중 가장 빠른 것으로 갱신
    if pop['A'] + pop['B'] + pop['C'] + pop['D'] == 0:
        now = min_time
        continue

    for alp in pop:
        # 도로에 진입한 차가 있고, 오른쪽 도로에 진입한 차가 없다면
        if pop[alp] and not pop[right[alp]]:
            time, index = road[alp].popleft()
            # answer에 빠져나온 시간 기록
            answer[index] = now

    now += 1

for a in answer:
    print(a)