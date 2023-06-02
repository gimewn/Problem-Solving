import sys
import heapq
from collections import deque

n = int(sys.stdin.readline())

classes = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

heapq.heapify(classes)

classroom = []

roomcnt = 0

while classes:
    now = heapq.heappop(classes)
    if classroom:
        if now[0] < classroom[0]:
            roomcnt += 1
        else:
            heapq.heappop(classroom)
    else:
        roomcnt += 1

    heapq.heappush(classroom, now[1])

print(roomcnt)
