from sys import stdin
import heapq

city_cnt = int(stdin.readline())
bus_cnt = int(stdin.readline())

city = [[2e9]*city_cnt for _ in range(city_cnt)]

bus = {}

for _ in range(bus_cnt):
    start, destination, cost = map(int, stdin.readline().split())
    start, destination = start-1, destination-1
    if start not in bus:
        bus[start] = {}
    if destination not in bus[start]:
        bus[start][destination] = 2e9
    bus[start][destination] = min(bus[start][destination], cost)

def dijkstra(bus_num):
    heap = []
    heapq.heappush(heap, (bus_num, 0))
    city[bus_num][bus_num] = 0

    while heap:
        now, now_cost = heapq.heappop(heap)
        if now in bus:
            for next_value in bus[now]:
                next_cost = bus[now][next_value]
                if city[bus_num][next_value] > now_cost + next_cost:
                    city[bus_num][next_value] = now_cost + next_cost
                    heapq.heappush(heap, (next_value, city[bus_num][next_value]))

for idx in range(city_cnt):
    if idx in bus:
        dijkstra(idx)

for i in range(city_cnt):
    for j in range(city_cnt):
        if city[i][j] == 2e9:
            print(0, end=" ")
        else:
            print(city[i][j], end=" ")
    print()