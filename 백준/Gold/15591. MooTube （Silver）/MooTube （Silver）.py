import sys
import heapq

def cal_reco(lst, standard):
    answer = 0
    for value in lst:
        if 2e9 > value >= standard:
            answer += 1
    return answer

def dijkstra(start):
    check = [2e9]*(N+1)
    check[start] = 0
    heap = []
    heapq.heappush(heap, (start, 2e9))
    while heap:
        now, cost = heapq.heappop(heap)
        for next_, value in board[now]:
            if check[next_] == 2e9:
                check[next_] = min(value, cost)
                heapq.heappush(heap, (next_, check[next_]))
    return check

inputs = sys.stdin.readline

N, Q = map(int, inputs().split())
board = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, inputs().split())
    board[a].append((b, c))
    board[b].append((a, c))

questions = []
quest_v = {}

for _ in range(Q):
    k, v = map(int, inputs().split())
    if v not in quest_v:
        quest_v[v] = []
    questions.append((k, v))

for key in quest_v:
    quest_v[key] = dijkstra(key)

for k, v in questions:
    print(cal_reco(quest_v[v], k))