import sys

N = int(sys.stdin.readline())

P = [0] + list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    for j in range(i+1, N+1):
        P[j] = max(P[j], P[i] + P[j-i])

print(P[-1])