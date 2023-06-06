# 플로이드 워셜 풀이

import sys

city_cnt = int(sys.stdin.readline())
bus_cnt = int(sys.stdin.readline())

city = [[2e9]*city_cnt for _ in range(city_cnt)]

def make_myself_zero(cnt):
    # 자기 자신으로 가는 경우를 0으로 갱신
    for y in range(cnt):
        city[y][y] = 0

def floyd_warshall(cnt):
    # i번째 도시를 경유하는 경우
    for i in range(cnt):
        for j in range(cnt):
            for k in range(cnt):
                # j에서 k로 바로 가는 것 VS j -> i -> k 로 i를 경유하는 것 비교
                city[j][k] = min(city[j][k], city[j][i] + city[i][k])

for _ in range(bus_cnt):
    a, b, c = map(int, sys.stdin.readline().split())
    # 시작 도시와 도착 도시를 연결하는 노선 중 최소 비용
    city[a-1][b-1] = min(city[a-1][b-1], c)

make_myself_zero(city_cnt)

floyd_warshall(city_cnt)

for y in range(city_cnt):
    for x in range(city_cnt):
        if city[y][x] < 2e9:
            print(city[y][x], end=" ")
        else:
            print(0, end=" ")
    print()