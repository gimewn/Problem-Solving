import sys

N, K = map(int, sys.stdin.readline().split())

bags = [[0]*(K+1) for _ in range(N)]

items = []

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    items.append((W, V))

items.sort()

for i in range(N):
    for j in range(K+1):
        if j < items[i][0]:
            bags[i][j] = bags[i-1][j]
        else:
            bags[i][j] = max(bags[i-1][j], bags[i-1][j-items[i][0]] + items[i][1])

print(bags[-1][-1])