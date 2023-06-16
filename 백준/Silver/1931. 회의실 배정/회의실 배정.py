import heapq
import sys

n = int(input())

meeting = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    heapq.heappush(meeting, (start, end))

lst = []

while meeting:
    start, end = heapq.heappop(meeting)

    if lst:
        cstart, cend = lst[-1]
        if cend > start and cend > end:
            lst.pop()
            lst.append((start, end))
        elif start >= cend:
            lst.append((start, end))
    else:
        lst.append((start, end))

print(len(lst))