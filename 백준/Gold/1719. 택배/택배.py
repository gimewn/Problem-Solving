import sys, heapq

N, M = map(int, sys.stdin.readline().split())

places = [[2e9]*(N+1) for _ in range(N+1)]
answer = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    s, e, cost = map(int, sys.stdin.readline().split())
    places[s][e] = cost
    places[e][s] = cost
    answer[s][e] = e
    answer[e][s] = s

for i in range(1, N+1):
    places[i][i] = 0
    answer[i][i] = '-'

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if places[i][j] > places[i][k] + places[k][j]:
                places[i][j] = places[i][k] + places[k][j]
                answer[i][j] = answer[i][k]

for row in answer[1:]:
    print(*row[1:])