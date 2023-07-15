import sys, heapq

inputs = sys.stdin.readline

N = int(inputs())

heap = []

for _ in range(N):
    lst = list(map(int, inputs().split()))
    if not heap:
        for value in lst:
            heapq.heappush(heap, value)
    else:
        for value in lst:
            if value > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, value)

print(heap[0])