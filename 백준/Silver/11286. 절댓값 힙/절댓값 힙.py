import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            now = heapq.heappop(heap)
            print(now[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))