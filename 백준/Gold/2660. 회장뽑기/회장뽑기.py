import heapq

n = int(input())

member = [[2e9]*(n+1) for _ in range(n+1)]
min_score = 2e9
candidate = set()

relation = {}

while True:
    one, two = map(int, input().split())
    if one < 0 and two < 0:
        break

    if one not in relation:
        relation[one] = []
    if two not in relation:
        relation[two] = []

    relation[one].append(two)
    relation[two].append(one)

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    member[start][start] = 0
    member[start][0] = 0

    while heap:
        cost, now = heapq.heappop(heap)

        for next in relation[now]:
            next_cost = cost + 1
            if next_cost < member[start][next]:
                member[start][next] = next_cost
                heapq.heappush(heap, (next_cost, next))

for mem in range(1, n+1):
    dijkstra(mem)
    min_score = min(min_score, max(member[mem]))

for idx in range(1, n+1):
    if max(member[idx]) == min_score:
        candidate.add(idx)

candidate = sorted(candidate)

print(min_score, len(candidate))
print(*candidate)