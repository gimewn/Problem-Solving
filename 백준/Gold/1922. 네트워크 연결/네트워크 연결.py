import sys
import heapq

def prim(start):
    heap = []
    check = [0]*N
    res = 0

    heapq.heappush(heap, (0, start))

    while heap:
        cost, now = heapq.heappop(heap)
        if not check[now]:
            check[now] = 1
            res += cost
            if now in computer:
                for value in computer[now]:
                    heapq.heappush(heap, (computer[now][value], value))
    return res

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

computer = {}
answer = 2e9

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    a, b = a-1, b-1

    if a not in computer:
        computer[a] = dict()
    if b not in computer[a]:
        computer[a][b] = 2e9

    if b not in computer:
        computer[b] = dict()
    if a not in computer[b]:
        computer[b][a] = 2e9

    computer[a][b] = min(computer[a][b], c)
    computer[b][a] = min(computer[b][a], c)

print(prim(0))