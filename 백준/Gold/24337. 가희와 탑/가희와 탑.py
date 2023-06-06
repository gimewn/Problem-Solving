from sys import stdin
from collections import deque

N, A, B = map(int, stdin.readline().split())

if A+B > N+1:
    print(-1)
else:

    building = deque()

    for num in range(1, A):
        building.append(num)

    building.append(max(A, B))

    for num in range(B-1, 0, -1):
        building.append(num)

    if len(building) == N:
        print(*building)
    else:
        print(building[0], end=" ")
        for _ in range(N-len(building)):
            print(1, end=" ")
        for idx in range(1, len(building)):
            print(building[idx], end=" ")