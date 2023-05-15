from collections import deque

n, w, l = map(int, input().split())

truck = deque(list(map(int, input().split())))

idx = 0

bridge = [0]*w

out_truck = 0

while truck or out_truck < n:
    idx += 1
    # 다리 맨 왼쪽에 트럭이 있으면 건너기
    if bridge[0]:
        bridge[0] = 0
        out_truck += 1
    # 1번 인덱스부터 트럭 앞으로 전진
    for y in range(1, w):
        if not bridge[y-1] and bridge[y]:
            bridge[y-1] = bridge[y]
            bridge[y] = 0
    if truck:
        # 현재 다리의 하중에 대기 중인 첫번째 트럭의 무게를 더했을 때 다리 최대 하중을 넘지 않으면
        if sum(bridge) + truck[0] <= l:
            bridge[-1] = truck.popleft()


print(idx)