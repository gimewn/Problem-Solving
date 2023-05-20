import math

H, W, N, M = map(int, input().split())

cols = math.ceil(W/(M+1))
rows = math.ceil(H/(N+1))

print(cols*rows)