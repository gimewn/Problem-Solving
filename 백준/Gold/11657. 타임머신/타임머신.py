import heapq
import sys
from collections import deque

inputs = sys.stdin.readline

def cal_fast_time():
    def bellman_ford(start):
        distance = [2e9]*(N+1)
        distance[start] = 0

        for turn in range(N):
            for departure, destination, value in edge:
                if distance[departure] != 2e9 and distance[departure] + value < distance[destination]:
                    if turn == N-1:
                        return False
                    distance[destination] = distance[departure] + value
        return distance

    N, M = map(int, inputs().split())

    edge = []

    for _ in range(M):
        A, B, C = map(int, inputs().split())
        edge.append((A, B, C))

    res = bellman_ford(1)

    if res:
        for idx in range(2, N+1):
            if res[idx] < 2e9:
                print(res[idx])
            else:
                print(-1)
    else:
        print(-1)

cal_fast_time()