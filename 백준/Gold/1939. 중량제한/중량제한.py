import sys
from collections import deque

def BFS(limit):
    q = deque([first])
    check = [0]*(N+1)
    check[first] = 1

    while q:
        now = q.popleft()
        if now == second:
            return True
        for next_island, cost in islands[now]:
            if check[next_island]:
                continue
            if cost < limit:
                continue
            check[next_island] = 1
            q.append(next_island)
    return False

N, M = map(int, sys.stdin.readline().split())

islands = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    islands[a].append((b, cost))
    islands[b].append((a, cost))

first, second = map(int, sys.stdin.readline().split())

start, end = 1, 1000000000

answer = 0

while start <= end:
    mid = (start + end) // 2
    if BFS(mid):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)