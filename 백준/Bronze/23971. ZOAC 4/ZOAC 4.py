import math

H, W, N, M = map(int, input().split())

if H % (N+1):
    rows = H // (N+1) + 1
else:
    rows = H // (N+1)

if W % (M+1):
    cols = W // (M+1) + 1
else:
    cols = W // (M+1)

print(cols*rows)