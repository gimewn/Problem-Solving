import sys
import heapq

inputs = sys.stdin.readline

def dijkstra(start, destination):
    check = [2e9]*(N+1)
    check[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        count, now = heapq.heappop(heap)

        for ncount, nvalue in eat[now]:
            if check[nvalue] > count + ncount:
                check[nvalue] = count + ncount
                heapq.heappush(heap, (count+ncount, nvalue))

    return check[-1]

N, M = map(int, inputs().split())

eat = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, inputs().split())
    heapq.heappush(eat[a], (c, b))
    heapq.heappush(eat[b], (c, a))

print(dijkstra(1, N))