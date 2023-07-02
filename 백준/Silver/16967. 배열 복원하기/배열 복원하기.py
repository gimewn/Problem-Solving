import sys

inputs = sys.stdin.readline

H, W, X, Y = map(int, inputs().split())

B = [list(map(int, inputs().split())) for _ in range(H+X)]

A = [[] for _ in range(H)]

for x in range(H):
    for y in range(W):
        if x >= X and y >= Y:
            B[x][y] -= B[x-X][y-Y]
        A[x].append(B[x][y])

for a in A:
    print(*a)